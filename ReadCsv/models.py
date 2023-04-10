from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length=20)
    
class StudentData(models.Model):
    file = models.FileField(upload_to='files')
    status = models.BooleanField(default=False)
    owner = models.CharField(max_length=30, null=True)
