from hashlib import new
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.TextField()
    contenido = models.TextField()
    fecha_publicación = models.DateField(auto_now_add=True)
    foto = models.ImageField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
    
    
class Comments(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.content[:10]
    
    
class Category(models.Model):
    name = models.CharField('Categoría', max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name