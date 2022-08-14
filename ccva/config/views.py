from django.shortcuts import render
from django.views.generic.list import ListView
from apps.post.models import Post


def index(request):
    return render(request, 'start.html')