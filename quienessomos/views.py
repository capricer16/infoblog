from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from quienessomos.models import Quienessomos

class Quienessomos(ListView):
    model = Quienessomos
    template_name = 'quienessomos.html'

    def Quienessomos(request):
        return render(request, 'quienessomos.html')