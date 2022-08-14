from django.shortcuts import render, redirect
from django.views.generic.list import ListView

class ListarPost(ListView):
    model = Post
    template_name = 'Post/listarPosts.html'