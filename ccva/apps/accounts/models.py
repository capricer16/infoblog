from datetime import datetime
from email.policy import default
from optparse import Option
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstracUser

from infoblog.ccva.config import settings

# Create your models here.
sex_choices= [ ("Masculino", "masculino"), ("Femenino","femenino")
]
class Register(models.Model):
    e_mail= models.EmailField(max_length=40, primary_key= True)
    password= models.ForeignKey(max_length=10)
    name= models.CharField(max_length=30)
    surname= models.CharField(max_length=30)
    dni= models.PositiveIntegerField(max_length=10)
    date_of_birth= models.DateTimeField(default)
    celphone= models.PositiveIntegerField(max_length=15)
    address= models.CharField(max_length=20)
    sex= models.Choices(sex_choices)
    city = models.CharField(maxlength=20, help_text= "Ingrese su ciudad")
    state_province = models.CharField(maxlength=20, help_text= "Ingrese su provincia")
    country = models.CharField(maxlength=20, help_text= "Ingrese su país")
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)


class CyC(models.Model):
    e_mail= models.ForeignKey(Register, settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date= models.DateTimeField(auto_now=True)


class Comment(models.Model):
    e_mail= models.ForeignKey(Register, settings.AUTH_USER_MODEL, on_delete=CASCADE)
    date= models.DateTimeField(auto_now=True)


class User(AbstracUser):
    """Extiende el Usuario de django"""
