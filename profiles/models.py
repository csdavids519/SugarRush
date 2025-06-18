from django.db import models
from django.contrib.auth.models import User
from checkout.models import Basket, ShippingInfo
from products.models import Product
from django.utils import timezone


class Customer(models.Model):
    """A model to collect user information"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer_username',
        null=True, blank=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Customer {self.user}"


class Order(models.Model):
    """Model to collect ordered products and attach associated shipping data"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='order_user',
        null=True,
        blank=True)
    basket_order = models.ForeignKey(Basket,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True)
    shipping_order = models.ForeignKey(ShippingInfo,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True)
    date = models.DateTimeField(default=timezone.now)


class Review(models.Model):
    """Model to collect user store and product reviews"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.TextField()
    rating = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Review by {self.user}"
