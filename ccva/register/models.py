from django.db import models
from django.conf import settings
from tkinter import CASCADE
from email.policy import default


class register(models.Model):
    e_mail= models.EmailField(max_length=40, primary_key= True)
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    dni= models.PositiveIntegerField()
    date_of_birth= models.DateTimeField(auto_now_add=True)
    celphone= models.PositiveIntegerField()
    address= models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state_province = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    
# Create your models here.
