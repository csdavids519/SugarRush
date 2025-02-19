from django.dispatch import receiver, Signal
from django.contrib.auth.models import User
from .models import Basket

basket_cleared_signal = Signal()

@receiver(basket_cleared_signal)
def clear_basket(sender, user, **kwargs):
    # Clear the basket when the signal is received
    try:
        basket = Basket.objects.get(user=user)
        basket.basket_products.all().delete() #deletes all BasketProduct records
    except Basket.DoesNotExist:
        pass
    print(f"BASKET SIGNAL TRIGGRED {user}")
