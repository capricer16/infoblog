from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from contacto.models import Contacto

class Contacto(ListView):
    model = Contacto
    template_name = 'contacto.html'

    def contacto(request):
        return render(request, 'contacto.html')