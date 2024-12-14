from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Inclui as URLs do app 'core'
]

from django.shortcuts import render

def home(request):
    nome_do_usuario = request.GET.get('nome', 'Visitante')  # Captura o nome pela URL ou usa "Visitante"
    return render(request, 'core/home.html', {'nome_do_usuario': nome_do_usuario})

import os

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Certifique-se de que "templates" está aqui
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

python manage.py runserver 0.0.0.0:8000