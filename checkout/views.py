from django.shortcuts import (
    render, redirect,
    )
from checkout.models import Basket
# Create your views here.


def checkout(request):
    """ A view to return the index page """
    baskets = Basket.objects.prefetch_related('basket_products__product')

    return render(request, 'checkout.html', {'baskets': baskets})
