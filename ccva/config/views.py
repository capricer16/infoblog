from django.shortcuts import render
from django.views.generic.list import ListView
from apps.post.models import Post

class Inicio(ListView):
    model = Post
    template_name = 'start.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        return context