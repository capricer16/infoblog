from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    contenido = models.TextField()
    fecha_publicación = models.DateField(auto_now_add=True)
    foto = models.ImageField()

    def __str__(self):
        return self.titulo

# Create your models here.
