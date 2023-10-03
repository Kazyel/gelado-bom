from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Picole, Sorvete, Acai, ShopCartPicole, ShopCartSorvete, ShopCartAcai

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


def update_picole(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Picole.objects.get(id=productId)
    cart, created = ShopCartPicole.objects.get_or_create(produto = product)
    if action == 'add':
        cart.quantidade = (cart.quantidade + 1)
    elif action == 'remove':
        cart.quantidade = (cart.quantidade - 1)
    
    cart.save()
    if cart.quantidade <= 0:
        cart.delete()

    return JsonResponse("Item was added", safe=False)

def update_sorvetes(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    product = Sorvete.objects.get(id=productId)
    cart, created = ShopCartSorvete.objects.get_or_create(produto = product)
    if action == 'add':
        cart.quantidade = (cart.quantidade + 1)
    elif action == 'remove':
        cart.quantidade = (cart.quantidade - 1)
    
    cart.save()
    if cart.quantidade <= 0:
        cart.delete()

    return JsonResponse("Item was added", safe=False)

def update_cart(request):
    return {'cartPicoles': ShopCartPicole.objects.all(), 
            'cartSorvetes': ShopCartSorvete.objects.all(),
            'cartAcais': ShopCartAcai.objects.all()}