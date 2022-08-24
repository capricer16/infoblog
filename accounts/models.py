from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from tkinter import CASCADE
from email.policy import default   
# Create your models here.

class User(AbstractUser):
    """Extiende el Usuario de django"""
    ADMIN = 'ADMIN'
    VISITANTE = 'VISITANTE'
    SOCIO = 'SOCIO'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SOCIO, 'Socio'),
        (VISITANTE, 'Visitante'),
    )
    role = models.CharField('Role', max_length=12, choices=ROLE_CHOICES, default=VISITANTE)
    dni= models.PositiveIntegerField("DNI", null=True, blank=False)
    date_of_birth= models.DateTimeField("Fecha de Nacimiento", null=True, blank=False)
    cellphone= models.PositiveIntegerField("Celular", null=True, blank=False)
    address= models.CharField("Direccion", max_length=30, null=True, blank=False)
    name= models.CharField("Nombre", max_length=30, null=True, blank=False)
    surname= models.CharField("Apellido", max_length=30, null=True, blank=False)
    e_mail= models.EmailField("Email", max_length=40, null=True, blank=False)

#sex_choices = ( "masculino"("Masculino", "masculino"), "femenino"("Femenino","femenino")
class register(models.Model):

    e_mail= models.EmailField(max_length=40, primary_key= True)
    #password= models.(max_length=20, on_delete=models.CASCADE)
    name= models.CharField(max_length=30, null=True, blank=False)
    surname= models.CharField(max_length=30, null=True, blank=False)
    dni= models.PositiveIntegerField()
    date_of_birth= models.DateTimeField(null=True, blank=False)
    cellphone= models.PositiveIntegerField()
    address= models.CharField(max_length=30, null=True, blank=False)
    #sex= models.Choices(sex_choices)
    city = models.CharField(max_length=20, help_text= "Ingrese su ciudad")
    state_province = models.CharField(max_length=20, help_text= "Ingrese su provincia")
    country = models.CharField(max_length=20, help_text= "Ingrese su país")
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
