from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from capacitacion.models import Capacitacion

def capacitacion(request):
    capacitacion = Capacitacion.objects.all()
    return render(request, 'capacitacion.html', {'capacitacion': capacitacion})

def capacitacion_detalles(request, pk):
    capacitacion = get_object_or_404(Capacitacion, id=pk)
    return render(request, 'detalles.html', {'capacitacion': capacitacion}) 