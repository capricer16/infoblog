from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('capacitaciones', views.capacitaciones, name='capacitaciones'),
    path('noticias', views.noticias, name='noticias'),
    path('quienessomos', views.quienessomos, name='quienessomos'),
]
