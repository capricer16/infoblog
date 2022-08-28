from django.contrib import admin
from django.urls import path
from . import views

app_name = "contacto"

urlpatterns = [
     path('', views.Contacto.as_view(), name='contacto'),
]