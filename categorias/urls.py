from django.contrib import admin
from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
     path('', views.categorias, name='categorias'),     
]