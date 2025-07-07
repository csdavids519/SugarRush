import uuid
import stripe

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Sum, F
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required 

from .forms import OrderForm
from .signals import order_placed_signal

from checkout.models import Basket, BasketProduct
from checkout.contexts import update_basket_total
from products.models import Product

@login_required
def checkout(request):
    """
    A view to render the checkout basket edit page with basket data
    """
    basket = None
    has_items = False
        
    if request.user.is_authenticated:
        try:
            basket = Basket.objects.filter(user=request.user).last()
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user=request.user)
            return render(request, 'checkout.html', {'basket_results': None, 'has_items': False})
        
        if basket and basket.basket_products.exists():
            has_items = True

    return render(request, 'checkout.html', {'basket_results': basket, 'has_items': has_items})

@login_required
def payment(request):
    """ A view to return the Stripe payment page """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Prevent double orders
        if request.session.get("order_processed"):
            return redirect('checkout:success')

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            request.session['purchase_id'] = str(uuid.uuid4())
            request.session['shipping_data'] = order_form.cleaned_data
            request.session['order_processed'] = True

            return redirect('checkout:success')

        else:
            messages.error(request, "Invalid form data. Please try again.")

    else:
        order_form = OrderForm()

    try:
        basket = Basket.objects.filter(user=request.user).last()
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=request.user)
        return render(request, 'payment.html', {'order_results': None})

    total_price = basket.basket_products.aggregate(
        total=Sum(F('product__price') * F('quantity'))
    )['total'] or 0

    stripe_total = round(total_price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'order_results': basket,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'payment.html', context)

@login_required
def success(request):
    """
    A view to render the success page and call order placed signal.
    Sends an email to customer that purchase was completed.
    """
    user = request.user

    basket = Basket.objects.filter(user=user).last()
    total_price = basket.basket_products.aggregate(
        total=Sum(F('product__price') * F('quantity'))
    )['total'] or 0

    shipping_data = request.session.get('shipping_data')

    # Call Signal
    order_placed_signal.send(
        sender=None,
        user=user,
        shipping_data=shipping_data
    )

    # Clean up session
    request.session.pop('shipping_data', None)
    request.session.pop('order_processed', None)
    request.session.pop('purchase_id', None)

    # Collect email data
    basket_items = basket.basket_products.select_related('product')

    purchase_details = {
        'user_name': user,
        'basket_items': basket_items,
        'total': total_price,
        'shipping': shipping_data,
    }

    # Email
    subject = 'SugarRush - Purchase Confirmation'

    html_message = render_to_string(
        'emails/purchase_confirmation.html',
        {'purchase_details': purchase_details}
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,
    )

    messages.success(request, 'Thanks for your purchase, your candy is on the way!')

    return render(request, 'success.html')


@login_required
def add_to_basket(request, item_id):
    """
    A view to add current product to the basket list
    -  find the users basket
    - check for existing matching products or create new
    - update total basket cost
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))

    try:
        basket = Basket.objects.filter(user=request.user).last()
    except Basket.DoesNotExist:
        basket = Basket.objects.create(user=request.user)

    try:
        basket_product = BasketProduct.objects.get(
            basket=basket,
            product=product
            )
        basket_product.quantity += quantity
        basket_product.save()

    except BasketProduct.DoesNotExist:
        basket_product, created = BasketProduct.objects.get_or_create(
                                        basket=basket,
                                        product=product
                                        )
        basket_product.quantity += quantity-1
        basket_product.save()

    update = update_basket_total(request)
    messages.success(request, 'Candy is in the bag!')

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)


@login_required
def update_basket(request, basket_product_id):
    """ Update user basket total """
    basket_list = get_object_or_404(BasketProduct, id=basket_product_id)

    if request.method == "POST":
        qty_update = int(request.POST.get("quantity", 1))
        if qty_update > 0:
            basket_list.quantity = qty_update
            basket_list.save()
            

    messages.success(request, 'Basket updated!')

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)


@login_required
def remove_from_basket(request, basket_product_id):
    """A view to manage item removal from basket"""
    basket_list = get_object_or_404(BasketProduct, id=basket_product_id)
    basket_list.delete()

    messages.success(request, 'Basket updated!')

    redirect_url = request.POST.get('redirect_url', '/')
    return redirect(redirect_url)

