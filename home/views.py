from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from products.models import ProductOrService
from django.shortcuts import render


# Create your views here.
# def home(request):
#     return render(request, 'home/index.html')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'products': ProductOrService.objects.all()[:10]
        }
        return render(request, 'home/productorservice.html', context=context)
