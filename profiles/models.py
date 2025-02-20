from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Basket, ShippingInfo
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_username', null=True, blank=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Customer {self.user}"


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', null=True, blank=True)
    basket_order = models.ForeignKey(Basket, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    shipping_order = models.ForeignKey(ShippingInfo, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
