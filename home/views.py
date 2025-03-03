from django.shortcuts import (render, get_object_or_404)
from products.models import Product


def index(request):
    """ A view to return the index page """
    promo_new = get_object_or_404(Product, pk=1)
    promo_popular_1 = get_object_or_404(Product, pk=4)
    promo_popular_2 = get_object_or_404(Product, pk=8)
    promo_popular_3 = get_object_or_404(Product, pk=6)

    context = {
        'promo_new': promo_new,
        'promo_popular_1': promo_popular_1,
        'promo_popular_2': promo_popular_2,
        'promo_popular_3': promo_popular_3,
    }
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")

    return render(request, 'index.html', context)
