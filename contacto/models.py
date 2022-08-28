from django.db import models


class Contacto(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    published_date = models.DateField(auto_now_add=True)
    email = models.CharField(max_length=75)
    cellphone= models.PositiveIntegerField("Celular", null=True, blank=False)


    def __str__(self):
        return self.firstName