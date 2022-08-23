from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from post.models import Post

class ListarPost(ListView):
    model = Post
    template_name = 'listarpost.html'

    def noticias(request):
        return render(request, 'listarpost.html')