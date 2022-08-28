from django.contrib import admin
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
     path('', views.post_list, name='post_list'),

     path('<int:pk>/', views.post_detallesdelpost, name='post_detallesdelpost'),
]