from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('capacitacion', include('capacitacion.urls')),
    path('post', include('post.urls')),
    path('quienessomos', views.quienessomos, name='quienessomos'),
    path('Iniciarsecion', views.iniciarsecion, name='iniciarsecion'),
]
