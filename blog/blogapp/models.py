from django.db import models
from django.contrib.auth.models import User

class ProfileUpdate(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.username)
    
class PostUpload(models.Model):
    post=models.ImageField(upload_to='posts/')
    def __str__(self):
        return '{}'.format(self.post)