from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.


class Orders(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                    null=True, blank=True)
    order_status = models.CharField(max_length=254)
    order_date = models.DateField()

    def __str__(self):
        return str(self.orders_id)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_username', null=True, blank=True)
    order_id = models.ForeignKey(Orders, on_delete=models.DO_NOTHING,
                                    null=True, blank=True)
    basket_id = models.ForeignKey('checkout.Basket', on_delete=models.SET_NULL,
                                    null=True, blank=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Customer {self.user}"
