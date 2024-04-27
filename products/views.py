from django.shortcuts import render
from django.views import View
from .models import ProductOrService


# Create your views here.
class ProductView(View):
    def get(self, request, slug, *args, **kwargs):
        product = ProductOrService.objects.get(slug=slug)
        content = {'product': product}
        return render(request, 'products/post.html', content)
