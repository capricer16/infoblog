from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from post.models import Post

# class ListarPost(ListView):
#     model = Post
#     template_name = 'listarpost.html'

#     def noticias(request):
#         return render(request, 'listarpost.html')

def post_list(request):
    posts = Post.objects.all()
    print(posts.query)
    return render(request, 'listarpost.html', {'posts': posts})

def post_detallesdelpost(request, pk):
    # buscamos el post y lo mostramos
    post = get_object_or_404(Post, id=pk)
    return render(request, 'detallesdelpost.html', {'post': post})