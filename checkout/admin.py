from django.contrib import admin
from .models import Basket, BasketProduct, ShippingInfo

# Register your models here.


class BasketProductInline(admin.TabularInline):
    model = BasketProduct
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_products']

    # Code reference chatGPT to create def git_products
    def get_products(self, obj):
        return ", ".join(f"{i.product.name} (x{i.quantity})" for i in obj.basket_products.all())
    get_products.short_description = "Products"


@admin.register(BasketProduct)
class BasketProductAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'email']
    readonly_fields = ['id',
                       'user',
                       'full_name',
                       'email',
                       'phone_number',
                       'country',
                       'postcode',
                       'town_or_city',
                       'street_address1',
                       'street_address2',
                       'state',
                       ]
