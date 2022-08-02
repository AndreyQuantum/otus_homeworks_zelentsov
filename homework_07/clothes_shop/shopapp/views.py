from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def index(request: HttpRequest):
    products = Product.objects.all()
    context = {
        "products" : products
    }
    return render(request, 'shopapp/index.html', context = context)

def details(request: HttpRequest, id: int):
    product = get_object_or_404(Product, pk=id)
    context = {
        "product" : product
    }
    return render(request, 'shopapp/details.html', context = context)
