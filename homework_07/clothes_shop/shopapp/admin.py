from django.contrib import admin
from .models import Product, ProductKind, Size
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'kind', 'description_short')
    list_display_links = ('id', 'name')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("kind")


class ProductKindAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_short')
    list_display_links = ('id', 'name')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'eu', 'usa', 'jpn')
    list_display_links = ('id', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductKind, ProductKindAdmin)
admin.site.register(Size, SizeAdmin)
