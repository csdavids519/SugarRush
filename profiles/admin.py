from django.contrib import admin
from .models import Customer

# Register your models here.


@admin.register(Customer)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'user',
                    'order_id',
                    'first_name',
                    'last_name',
                    ]

    fields = ['first_name',
              'last_name',
            ]

