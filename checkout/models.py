# models code reference, from ChatGPT
from django.db import models
from products.models import Product


class Basket(models.Model):
    basket_id = models.IntegerField(unique=True, null=False)

    def __str__(self):
        return f"Basket {self.basket_id}"


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='basket_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='basket_products')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in Basket {self.basket.basket_id}"
