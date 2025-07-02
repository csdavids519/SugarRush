from django.dispatch import Signal, receiver

from .models import Basket
from profiles.models import Customer, Order


basket_cleared_signal = Signal()


@receiver(basket_cleared_signal)
def clear_basket(sender, user, **kwargs):
    """
    Signal to clear the users basket after purchase complete
    """
    try:
        customer = Customer.objects.get(user=user)
        basket = Basket.objects.filter(user=user).first()
        basket = Basket.objects.create(user=user) 
        customer.basket_id = basket
        customer.save()
    except Basket.DoesNotExist:
        pass


order_placed_signal = Signal()


@receiver(order_placed_signal)
def create_order_and_new_basket(sender, user, shipping_data, **kwargs):
    """
    Signal to combine ordered products and shipping info
    creates a new basket for customers next order maintaining previous history
    """
    basket = Basket.objects.filter(user=user).last()
    if not basket:
        return

    Order.objects.create(
        user=user,
        basket_order=basket,
        full_name=shipping_data.get('full_name'),
        email=shipping_data.get('email'),
        phone_number=shipping_data.get('phone_number'),
        street_address1=shipping_data.get('street_address1'),
        street_address2=shipping_data.get('street_address2'),
        town_or_city=shipping_data.get('town_or_city'),
        postcode=shipping_data.get('postcode'),
        country=shipping_data.get('country'),
    )

    Basket.objects.create(user=user)
