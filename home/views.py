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
		posts = Post.objects.all().order_by('-id')[:5]
		capacitacion = Capacitacion.objects.all().order_by('-id')[:3]
		context['capacitacion'] = capacitacion
		primeros = [posts[0], posts[1], posts[2]]
		ultimos = [posts[3], posts[4], posts[5]]
		context['primeros'] = primeros
		context['ultimos'] = ultimos
		print(context)
		
		return context
def quienessomos(request):
    return render(request, 'home/quienessomos.html')

def iniciarsecion(request):
    return render(request, 'home/iniciarsecion.html')  

