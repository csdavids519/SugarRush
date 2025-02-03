from django.db import models


# Create your models here.
class Basket(models.Model):
    basket_id = models.IntegerField(unique=True)
    product_id = models.ForeignKey('products.Product', on_delete=models.SET_NULL,
                                    null=True, blank=True)
    customer_id = models.ForeignKey('profiles.Customer', on_delete=models.SET_NULL,
                                    null=True, blank=True)

    def __str__(self):
        return str(self.basket_id)