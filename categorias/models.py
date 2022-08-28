from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField( max_length=120)
    foto = models.ImageField(upload_to = 'categoria')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

