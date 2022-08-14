from django.contrib import admin
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.ListarPost.as_view(), name="listarPosts"),
]