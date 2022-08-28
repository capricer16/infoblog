from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', include('contacto.urls')),
    path('capacitacion', include('capacitacion.urls')),
    path('post', include('post.urls')),
     path('quienessomos', include('quienessomos.urls')),
    path('Iniciarsecion', views.iniciarsecion, name='iniciarsecion'),
]
