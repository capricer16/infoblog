from django.contrib import admin
from django.urls import path
from . import views

app_name = "capacitacion"

urlpatterns = [
    path('', views.capacitacion, name='capacitacion'),

    path('<int:pk>/', views.capacitacion_detalles, name='capacitacion_detalles'),
]
     