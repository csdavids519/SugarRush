from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
]
