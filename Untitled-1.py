
from django.shortcuts import render

def inicio(request):
    return render(request, 'core/inicio.html')


from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]


from django.shortcuts import render

def inicio(request):
    usuario_nome = "Luuh"  
    return render(request, 'core/inicio.html', {'nome_do_usuario': usuario_nome})