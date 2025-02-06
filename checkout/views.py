from django.shortcuts import (
    render, redirect,
    )
from checkout.models import Basket
# Create your views here.


def checkout(request):
    """ A view to return the index page """

    context = {
        'basket_list': Basket,
    }

    return render(request, 'checkout.html', context)
