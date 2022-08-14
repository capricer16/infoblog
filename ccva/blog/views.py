from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from blog.models import Post


class ListarPost(ListView):
    model = Post
    template_name = 'Post/listarPosts.html'
# Create your views here.
