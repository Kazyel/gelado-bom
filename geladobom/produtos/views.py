from django.shortcuts import render
from .models import Picole, Sorvete, Acai

# Create your views here.

def home(request):
    return render(request, 'home.html')

def picoles(request):
    Picoles = Picole.objects.all()
    return render(request, 'picoles.html', {'picoles': Picoles})

def sorvetes(request):
    Sorvetes = Sorvete.objects.all()
    Acais = Acai.objects.all()
    return render(request, 'sorvetes-acai.html', {'sorvetes': Sorvetes, 'acais': Acais})
