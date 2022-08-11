from django.shortcuts import render, get_object_or_404
from .models import Product, ProductKind
from django.views.generic import ListView, DetailView
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.select_related("kind")
    context_object_name = 'products'
    template_name = 'shopapp/index.html'

class KindListView(ListView):
    model = ProductKind
    context_object_name = 'kinds'
    template_name = 'shopapp/sort_kind.html'

class ProductKindListView(ListView):
    queryset = Product.objects.select_related("kind")
    context_object_name = 'products'
    template_name = 'shopapp/goods_by_kind.html'

    def get_queryset(self):
        qs = super().get_queryset()
        kind: ProductKind = get_object_or_404(ProductKind, name=self.kwargs["kind_name"])
        return qs.filter(kind__name=kind.name)

class ProductDetailView(DetailView):
    template_name = 'shopapp/details.html'
    context_object_name = 'product'
    queryset = Product.objects.select_related("kind").prefetch_related("size")
