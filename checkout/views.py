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


def payment(request):
    """ A view to return the checkout page """
    # find the basket based on user name
    try:
        basket = Basket.objects.get(user=request.user)
        print('payment: basket found')
    except Basket.DoesNotExist:
        print('payment: basket does not exist')
        basket = Basket.objects.create(user=request.user)
        return render(request, 'payment.html', {'order_results': None})
    return render(request, 'payment.html', {'order_results': basket})


def update_basket(request, basket_product_id):
    basket_list = get_object_or_404(BasketProduct, id=basket_product_id)

    if request.method == "POST":
        qty_update = int(request.POST.get("quantity", 1))
        if qty_update > 0:
            basket_list.quantity = qty_update
            basket_list.save()

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)


def remove_from_basket(request, basket_product_id):
    basket_list = get_object_or_404(BasketProduct, id=basket_product_id)
    basket_list.delete()

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)
