from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('orders/', views.order_history, name='order_history'),

]
