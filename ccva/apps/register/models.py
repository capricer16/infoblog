from django.db import models
from django.conf import settings
from tkinter import CASCADE
from email.policy import default

sex_choices= [ ("Masculino", "masculino"), ("Femenino","femenino")
]
class register(models.Model):
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
# Create your models here.
