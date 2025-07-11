from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('payment/', views.payment, name='payment'),
    path('success/', views.success, name='success'),
    path('basket/update/<int:basket_product_id>/',
         views.update_basket,
         name='update_basket'),
    path('basket/remove/<int:basket_product_id>/',
         views.remove_from_basket,
         name='remove_from_basket'),
]
