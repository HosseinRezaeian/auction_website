from django.urls import path
from .views import my_ajax_view

urlpatterns = [
    path('ajax/', my_ajax_view, name='my_ajax_view'),
]