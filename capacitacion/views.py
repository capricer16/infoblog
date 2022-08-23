from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from capacitacion.models import Capacitacion

class Capacitacion(ListView):
    model = Capacitacion
    template_name = 'capacitacion.html'

    def capacitacion(request):
        return render(request, 'capacitacion.html')