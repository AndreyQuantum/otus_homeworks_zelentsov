from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def index(request: HttpRequest):
    products = Product.objects.select_related("kind").order_by('id').all()
    context = {
        "products" : products
    }
    return render(request, 'shopapp/index.html', context = context)

def details(request: HttpRequest, id: int):
    product = get_object_or_404(Product.objects.select_related("kind"), pk=id)
    context = {
        "product" : product
    }
    return render(request, 'shopapp/details.html', context = context)
