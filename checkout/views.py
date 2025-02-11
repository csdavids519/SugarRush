from django.shortcuts import (
    render, redirect, get_object_or_404
    )
from checkout.models import Basket, BasketProduct
from products.models import Product

# Create your views here.


def checkout(request):
    """ A view to return the index page """
    # find the basket based on user name
    try:
        basket = Basket.objects.get(user=request.user)
        print('checkout: basket found')
    except Basket.DoesNotExist:
        print('checkout: basket does not exist')
        basket = Basket.objects.create(user=request.user)
        return render(request, 'checkout.html', {'basket_results': None})
    return render(request, 'checkout.html', {'basket_results': basket})


def add_to_basket(request, item_id):
    """ A view to add current product to the basket list """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))
    print(f'qty: {quantity}')

    # find the basket based on user name
    try:
        basket = Basket.objects.get(user=request.user)
        print('add_to_basket: basket found')
    except Basket.DoesNotExist:
        print('add_to_basket: basket does not exist')
        basket = Basket.objects.create(user=request.user)

    # check for existing matching products or create new
    try:
        basket_product = BasketProduct.objects.get(basket=basket, product=product)
        basket_product.quantity += quantity
        basket_product.save()
    # when new item is added to basket, subtract qty 1 from customer requested qty    
    except BasketProduct.DoesNotExist:
        basket_product, created = BasketProduct.objects.get_or_create(basket=basket, product=product)
        basket_product.quantity += quantity-1
        basket_product.save()

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)
