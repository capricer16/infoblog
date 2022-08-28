from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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
    dni = models.CharField('DNI', max_length=12, null=True, blank=True)
    address = models.CharField('Domicilio', max_length=30, null=True, blank=True)
    date_of_birth= models.DateTimeField("Fecha de Nacimiento", null=True, blank=False)
    cellphone= models.PositiveIntegerField("Celular", null=True, blank=False)
    name= models.CharField("Nombre", max_length=30, null=True, blank=False)
    surname= models.CharField("Apellido", max_length=30, null=True, blank=False)
    e_mail= models.EmailField("Email", max_length=40, null=True, blank=False)
    city = models.CharField("Ciudad", max_length=20)
    state_province = models.CharField("Provincia", max_length=20)
    country = models.CharField("Pais", max_length=20)
# class UserProfile(models.Model):
#     ADMIN = 'ADMIN'
#     VISITANTE = 'VISITIANTE'
#     SOCIO = 'SOCIO'

#     ROLE_CHOICES = (
#         (ADMIN, 'Admin'),
#         (SOCIO, 'Socio'),
#         (VISITANTE, 'Visitante'),
#     )

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')

#     role = models.CharField('Role', max_length=12, choices=ROLE_CHOICES, default=VISITANTE)
#     dni = models.CharField('DNI', max_length=12, null=True, blank=True)