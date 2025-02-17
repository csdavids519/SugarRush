import stripe
from django.shortcuts import (
    render, redirect, get_object_or_404
    )

from django.conf import settings
from django.http import JsonResponse

from checkout.models import Basket, BasketProduct
from products.models import Product

from .models import Orders
from .forms import OrderForm

from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


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
    order_form = OrderForm()

    # find the basket based on user name
    try:
        basket = Basket.objects.get(user=request.user)
        print('payment: basket found')
    except Basket.DoesNotExist:
        print('payment: basket does not exist')
        basket = Basket.objects.create(user=request.user)
        return render(request, 'payment.html', {'order_results': None})
    return render(request, 'payment.html', {'order_results': basket, 'order_form': order_form})


def submit_payment(request):
    if request.method == "POST":
        order_form = Orders(request.POST)

        if order_form.is_valid():
            print(order_form.fields)  # Debugging

    return render(request, 'checkout.html')


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


@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        YOUR_DOMAIN = 'http://localhost:8000'
        try:
            session = stripe.checkout.Session.create(
                ui_mode = 'embedded',
                line_items=[{
                    'price_data': {
                        'currency': 'euro',
                        'product_data': {
                            'name': 'T-shirt',
                        },
                        'unit_amount': 2000,  # Amount in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                return_url=YOUR_DOMAIN + '/return.html?session_id={CHECKOUT_SESSION_ID}',
            )
            return JsonResponse({"clientSecret": session.client_secret})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


def session_status(request):
    session_id = request.GET.get("session_id")
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
        return JsonResponse({
            "status": session.status,
            "customer_email": session.customer_details.email if session.customer_details else None
        })
    return JsonResponse({"error": "Session ID required"}, status=400)
