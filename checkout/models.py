import uuid

from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()
    
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


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
