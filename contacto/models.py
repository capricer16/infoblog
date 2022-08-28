from django.db import models

class Contacto(models.Model):
    cellphone= models.PositiveIntegerField("Celular", null=True, blank=False)
    name= models.CharField("Nombre", max_length=30, null=True, blank=False)
    surname= models.CharField("Apellido", max_length=30, null=True, blank=False)
    email = models.EmailField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

