# models code reference, from ChatGPT
from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Basket {self.user}"


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_products')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in Basket {self.basket.user}"


class Orders(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    state = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)













    def __str__(self):
        return self

