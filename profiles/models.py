from django.db import models
from products.models import Products


# Create your models here.
class Orders(models.Model):
    order_id = models.IntegerField(unique=True, null=True, blank=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    order_status = models.CharField(max_length=254)
    order_date = models.DateField()

    def __str__(self):
        return str(self.order_id)


class Wishlist(models.Model):
    wishlist_id = models.IntegerField(unique=True, null=True, blank=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL,
                                    null=True, blank=True)

    def __str__(self):
        return str(self.wishlist_id)


class Customer(models.Model):
    customer_id = models.IntegerField(unique=True, null=True, blank=True)
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING,
                                    null=True, blank=True)
    wishlist_id = models.ForeignKey(Wishlist, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    basket_id = models.ForeignKey('checkout.Basket', on_delete=models.SET_NULL,
                                    null=True, blank=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.customer_id)
