from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import ProductOrService, Picture
from auctions_product.models import Auctions_user_product


# Create your views here.
class ProductView(View):

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(ProductOrService, slug=slug)

        pic = Picture.objects.filter(parent=product)
        participated = False
        win_now = False
        if request.user.is_authenticated:
            try:
                is_in_mozaiedh = Auctions_user_product.objects.get(user=request.user, product=product)
                if is_in_mozaiedh:
                    participated = is_in_mozaiedh
                    win_now = Auctions_user_product.objects.filter(product=product).order_by('-price')[0]

            except:
                participated = False

        content = {'product': product, 'pictures': pic if pic else [], 'participated': participated, 'win_now': win_now}
        return render(request, 'products/post.html', content)
