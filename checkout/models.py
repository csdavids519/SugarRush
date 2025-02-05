# models code reference, from ChatGPT

from django.db import models
from django.db.models import Sum


class Basket(models.Model):
    basket_id = models.IntegerField(unique=True)
    products = models.ManyToManyField(
        'products.Product', through='BasketItem', related_name='baskets'
    )
    basket_customer = models.ForeignKey(
        'profiles.Customer', on_delete=models.SET_NULL, 
        null=True, blank=True
    )
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def update_total(self):
        """
        Update grand total based on product prices in the basket.
        """
        self.grand_total = self.basket_items.aggregate(
            total_price=Sum('lineitem_total')
        )['total_price'] or 0
        self.save()

    def __str__(self):
        return f"Basket {self.basket_id}"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def lineitem_total(self):
        """
        Calculate total price for this basket item.
        """
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
