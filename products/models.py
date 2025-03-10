from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    """A model to store product details"""
    FLAVOR = (
        ('Sour', 'Sour'),
        ('Sweet', 'Sweet'),
        ('Fruity', 'Fruity'),
    )

    TYPE = (
        ('Sticky', 'Sticky'),
        ('Hard', 'Hard'),
        ('Gummy', 'Gummy'),
        ('Chocolate', 'Chocolate'),
    )

    product_id = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=254)
    image = CloudinaryField('image', null=True, blank=True) 
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    description = models.TextField(null=True, blank=True)
    flavor = models.CharField(max_length=254,
                              blank=True,
                              null=True,
                              choices=FLAVOR
                              )
    type = models.CharField(max_length=254,
                            blank=True,
                            null=True,
                            choices=TYPE
                            )

    def __str__(self):
        return str(self.product_id)
