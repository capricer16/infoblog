from pyexpat import model
from django.db import models
from django.conf import settings

# Create your models here.



class Post(models.Model):
    imagen = models.ImageField(upload_to='images/')
    title = models.CharField('Título', max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

