from django.contrib import admin
from .models import Basket, BasketProduct

# Register your models here.


class BasketProductInline(admin.TabularInline):
    model = BasketProduct
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['basket_id', 'get_products']
    inlines = [BasketProductInline]

    #Code reference chatGPT to create def git_products
    def get_products(self, obj):
        return ", ".join(f"{bp.product.name} (x{bp.quantity})" for bp in obj.basket_products.all())
    get_products.short_description = "Products"

    