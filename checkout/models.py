from django.db import models
from django.contrib.auth.models import User
from products.models import Product


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
    