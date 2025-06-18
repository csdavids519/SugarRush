from django.shortcuts import (render, get_object_or_404)
from products.models import Product
from profiles.models import Review


def index(request):
    """ A view to return the index page """
    promo_new = get_object_or_404(Product, pk=1)
    promo_popular_1 = get_object_or_404(Product, pk=4)
    promo_popular_2 = get_object_or_404(Product, pk=8)
    promo_popular_3 = get_object_or_404(Product, pk=6)
    reviews = Review.objects.all().order_by('-updated')

    context = {
        'promo_new': promo_new,
        'promo_popular_1': promo_popular_1,
        'promo_popular_2': promo_popular_2,
        'promo_popular_3': promo_popular_3,
        'reviews': reviews,
    }

    return render(request, 'index.html', context)
