from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=254)
    product_image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    stocked = models.BooleanField(default=False, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=254,blank=True, null=True)

    def __str__(self):
        return str(self.product_id)
