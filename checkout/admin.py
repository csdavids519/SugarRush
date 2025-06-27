from django.contrib import admin
from .models import Basket, BasketProduct


class BasketProductInline(admin.TabularInline):
    """Arrange basket product inline style"""
    model = BasketProduct
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """Register basket admin module"""
    list_display = ['id', 'user', 'get_products']

    def get_products(self, obj):
        """
        Code reference chatGPT to create def git_products
        Find all products in basket and join with name and quantity
        """
        return ", ".join(
            f"{i.product.name} (x{i.quantity})"
            for i in obj.basket_products.all()
            )
    get_products.short_description = "Products"


@admin.register(BasketProduct)
class BasketProductAdmin(admin.ModelAdmin):
    """Register basket product module"""
    list_display = ['id']

