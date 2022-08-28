from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView



def categorias(request):
    categorias = Categorías.objects.all()
    print(categorias.query)
    return render(request, 'categorias.html', {'categorias': categorias})

