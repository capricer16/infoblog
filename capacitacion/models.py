from django.db import models

class Capacitacion(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    contenido = models.TextField()
    fecha_publicación = models.DateField(auto_now_add=True)
    foto = models.ImageField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title