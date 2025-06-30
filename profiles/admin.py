from django.contrib import admin
from .models import Customer, Order, Review


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
                    'get_shipping_address',
                    'get_products',
                    'date'
                    ]
    readonly_fields = ['id',
                       'user',
                       'get_shipping_address',
                       'get_products',
                       'date'
                       ]
    ordering = ['id']

    def get_products(self, obj):
        """
        find all basket products with quantity
        # Code reference chatGPT to create def get_products
        """
        if not obj.basket_order:
            return "No basket"
        return ", ".join(
            f"{i.product.name} (x{i.quantity})"
            for i in obj.basket_order.basket_products.all()
        )
        
    def get_shipping_address(self, obj):
        """Return formatted shipping address"""
        parts = [
            obj.street_address1,
            obj.street_address2,
            obj.town_or_city,
            obj.postcode,
            str(obj.country),
        ]
        return ", ".join(filter(None, parts))
    get_shipping_address.short_description = 'Shipping Address'



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'created',
                    'updated',
                    ]
    ordering = ['updated']