from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'home/index.html')

def contacto(request):
    return render(request, 'home/contacto.html')

def capacitaciones(request):
    return render(request, 'home/capacitaciones.html')

def quienessomos(request):
    return render(request, 'home/quienessomos.html')

def iniciarsecion(request):
    return render(request, 'home/iniciarsecion.html')  