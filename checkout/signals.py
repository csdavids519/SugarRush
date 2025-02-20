from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from .models import Basket, ShippingInfo
from profiles.models import Customer, Orders

basket_cleared_signal = Signal()

@receiver(basket_cleared_signal)
def clear_basket(sender, user, **kwargs):
    # Clear the basket when the signal is received
    try:
        customer = Customer.objects.get(user=user)
        basket = Basket.objects.filter(user=user).first()
        # basket.basket_products.all().delete() #deletes all BasketProduct records
        basket = Basket.objects.create(user=user) # create a new empty basket after purchase

        # Link basket to the customer
        customer.basket_id = basket
        customer.save()
    except Basket.DoesNotExist:
        pass
    print(f"BASKET SIGNAL TRIGGRED {user}")


order_placed_signal = Signal()

@receiver(order_placed_signal)
def create_order_and_new_basket(sender, user, shipping_info_id, **kwargs):
    try:
        # Get the user's current basket
        print('GET CURRENT BASKET')
        basket = Basket.objects.filter(user=user).last()  # Get the latest active basket

        if not basket:
            print(f"No active basket found for user {user}")
            return

        # Get the shipping info
        try:
            print('GET SHIPPING INFO')
            shipping_info = ShippingInfo.objects.get(id=shipping_info_id)
        except ShippingInfo.DoesNotExist:
            print(f"Shipping info not found for user {user}")
            return

        # Create a new Order instance
        print('CREATE NEW ORDER INSTANCE')
        order = Orders.objects.create(
            user=user,
            basket_order=basket,
            shipping_order=shipping_info
        )

        print(f"Order created: {order.id} for user {user}")

        # Create a new empty Basket instance for the user
        new_basket = Basket.objects.create(user=user)
        print(f"New basket created for user {user}")

    except Exception as e:
        print(f"Error in order signal: {e}")
