from django.shortcuts import render
from django.views.generic.list import ListView
from post.models import Post
from capacitacion.models import Capacitacion


# Create your views here.

class Inicio(ListView):
	model = Post
	template_name = 'home/index.html'
 
	def get_context_data(self, **kwargs):
		context = super(Inicio, self).get_context_data(**kwargs)
		posts = Post.objects.all().order_by('-id')[:6]
		context['ListadoPosts'] = posts
		capacitacion = Capacitacion.objects.all().order_by('-id')[:3]
		context['capacitacion'] = capacitacion
		
		
		return context
def quienessomos(request):
    return render(request, 'home/quienessomos.html')

def iniciarsecion(request):
    return render(request, 'home/iniciarsecion.html')  

