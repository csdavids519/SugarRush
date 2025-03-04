from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Basket(models.Model):
    """ Models for customer Baskets """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='basket',
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Basket {self.user}"


class BasketProduct(models.Model):
    """ Model for products and tracking quantity"""
    basket = models.ForeignKey(Basket,
                               on_delete=models.CASCADE,
                               related_name='basket_products')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='products_in_basket')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in Basket {self.basket.user}"


class ShippingInfo(models.Model):
    """
    Model to track customer shipping info
    Used to pre fill shipping forms and available to display user order history
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='shipping_user',
                             null=True,
                             blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.full_name
