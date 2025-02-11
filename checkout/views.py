from django.shortcuts import (
    render, redirect, get_object_or_404
    )
from checkout.models import Basket, BasketProduct
from products.models import Product

# Create your views here.


def checkout(request):
    """ A view to return the index page """
    baskets = Basket.objects.prefetch_related('basket_products__product')

    return render(request, 'checkout.html', {'baskets': baskets})


def add_to_basket(request, item_id):
    """ A view to add current product to the basket list """
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity', 1))

    # find the basket based on user name
    try:
        basket = Basket.objects.get(user=request.user)
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=request.user)

        # check for existing matching products or create new
        basket_product, created = BasketProduct.objects.get_or_create(basket=basket, product=product)

        basket_product.quantity += quantity
        basket_product.save()

        redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)
