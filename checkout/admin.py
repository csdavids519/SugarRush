from django.contrib import admin
from .models import Basket, BasketItem

# Register your models here.


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['basket_id',
                    'grand_total',
                    ]


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ['basket',
                    'product',
                    'quantity',
                    ]
