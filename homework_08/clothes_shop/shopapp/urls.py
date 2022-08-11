from django.urls import path, include

from .views import ProductListView, ProductKindListView, ProductDetailView, KindListView

app_name = "shopapp"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("by_type/", KindListView.as_view(), name='sort_by_kind'),
    path('<int:pk>/', ProductDetailView.as_view(), name="details"),
    path("by_type/<str:kind_name>", ProductKindListView.as_view(), name="kind_list"),
]
