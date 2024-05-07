from django.urls import path
from .views import ProductView

urlpatterns = [
    path('product/<slug:slug>', ProductView.as_view(), name='product')
]
