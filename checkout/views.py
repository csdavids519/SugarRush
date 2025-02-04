from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from products.models import Product
from django.contrib import messages

# Create your views here.


def checkout(request):
    """ A view to return the index page """

    return render(request, 'checkout.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
    
    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)

