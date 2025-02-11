from django.db import models
from django.contrib.auth.models  import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Blogmodel(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(null=True)
    User_ID =models.ForeignKey(User,on_delete=models.CASCADE)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    blog = models.ForeignKey(Blogmodel,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    Created= models.DateField(auto_now_add=True)

    body= models.TextField(null= True)
   
class Meta:
    ordering=['-Created']