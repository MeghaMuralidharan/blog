from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.http import Http404
from .forms import *
from .models import*

# Create your views here.

def login(request):
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('fullname')
        email=request.POST.get('mobile')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"The username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info("The mail is already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
                user.save()
                return redirect('index')
        else:
            messages.info('This password is not matching')
            return redirect(register)
    return render(request,'register.html')

def index(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'Please provide correct details')
            return redirect('index')
    return render(request,'index.html')

def profile(request):
    posts=PostUpload.objects.all()
    return render(request,'profile.html',{'posts':posts})

def logout(request):
    auth.logout(request)
    return redirect('index')

def myprofile(request):
    images=ProfileUpdate.objects.all()
    posts=PostUpload.objects.all()
    return render(request,'myprofile.html',{'images':images,'posts':posts})


def upload(request):
    posts=PostUpload.objects.all()
    if request.method=='POST':
        form=PostUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form=PostUploadForm()
    return render(request,'upload.html',{'form':form,'posts':posts})

def edit_profile(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myprofile')
    else:
        form=ProfileForm()
    return render(request, 'edit.html',{'form':form})

def delete(request,post_id):
    post=get_object_or_404(PostUpload,id=post_id)
    if request.method=='POST':
        post.delete()
        return redirect('myprofile')
    else:
        return Http404("Invalid")