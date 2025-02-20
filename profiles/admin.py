from django.contrib import admin
from .models import Customer, Orders


@admin.register(Customer)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'first_name',
                    'last_name',
                    ]
    ordering = ['id']


@admin.register(Orders)
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

    # Code reference chatGPT to create def git_products
    def get_products(self, obj):
        return ", ".join(f"{i.product.name} (x{i.quantity})" for i in obj.basket_order.basket_products.all())
