from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from .models import Basket, ShippingInfo
from profiles.models import Customer, Orders
from django.contrib.auth.models import User

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
def create_order_and_new_basket(sender, user, shipping_info_id, **kwargs):
    """ 
    Signal to combine ordered products and shipping info
    creates a new basket for customers next order maintaining previous history
    """

    basket = Basket.objects.filter(user=user).last()
    if basket:
        shipping_info = ShippingInfo.objects.get(id=shipping_info_id)

        order = Orders.objects.create(
            user=user,
            basket_order=basket,
            shipping_order=shipping_info
        )

        new_basket = Basket.objects.create(user=user)
        print('SIGNAL PY WORKING!')