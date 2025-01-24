from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileUpdate
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class PostUploadForm(forms.ModelForm):
    class Meta:
        model=PostUpload
        fields='__all__'