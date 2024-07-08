import datetime

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Auctions_user_product
from products.models import ProductOrService,Picture
from django.utils import timezone
from django.template.loader import render_to_string


@csrf_exempt
@require_POST
def my_ajax_view(request):
    if request.user.is_authenticated:
        slug = request.POST.get('slug')
        price = request.POST.get('price', 0)  # Default to 0 if not provided

        product = get_object_or_404(ProductOrService, slug=slug)

        try:
            price = int(price)
        except ValueError:
            return HttpResponse("Invalid price", status=400)

        if not Auctions_user_product.objects.filter(user=request.user, product=product):
            mozayedh = Auctions_user_product.objects.create(
                user=request.user,
                product=product,
                price=product.base_price,
                datetime=timezone.now()
            )
            mozayedh.save()



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

        return render(request, 'products/reload post.html', content)
    else:
        return HttpResponse("User not authenticated", status=401)
