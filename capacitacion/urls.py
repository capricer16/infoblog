from django.contrib import admin
from django.urls import path
from . import views

app_name = "capacitacion"

urlpatterns = [
     path('', views.Capacitacion.as_view(), name='capacitacion'), 
     ]