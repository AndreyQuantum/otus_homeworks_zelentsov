from django.urls import path, include

from .views import index, details
app_name = "shopapp"

urlpatterns = [
    path('', index, name="list"),
    path('<int:id>/', details, name="details"),
]