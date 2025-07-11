from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from checkout.models import Basket
from .models import Customer


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """Signal creates new basket on new user signup """
    if created:
        customer = Customer.objects.create(user=instance)
        basket = Basket.objects.create(user=instance)

        customer.basket_id = basket
        customer.save()

