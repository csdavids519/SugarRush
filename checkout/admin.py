from django.contrib import admin
from .models import Basket, BasketProduct, Orders

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

