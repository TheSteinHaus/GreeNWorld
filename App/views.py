from django.shortcuts import render
from .models import Product


def Home(request):
    products = Product.objects
    return render(request, 'base.html', {'products': products})


def Map(request):
    return render(request, 'map.html', {'title': 'Карта'})


def Card(request):
    return render(request, 'cardflip.html', {'title': 'Карточка продукта'})
