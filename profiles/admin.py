from django.contrib import admin
from .models import Customer, Order


@admin.register(Customer)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'first_name',
                    'last_name',
                    ]
    ordering = ['id']


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'basket_order',
                    'shipping_order',
                    'get_products',
                    'date'
                    ]
    readonly_fields = ['id',
                       'user',
                       'basket_order',
                       'shipping_order',
                       'get_products',
                       'date'
                       ]
    ordering = ['id']

    def get_products(self, obj):
        """
        find all basket products with quantity
        # Code reference chatGPT to create def get_products
        """
        return ", ".join(
            f"{i.product.name} (x{i.quantity})"
            for i in obj.basket_order.basket_products.all())
