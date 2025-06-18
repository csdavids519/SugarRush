from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('reviews', views.review_list, name='review_list'),
    path('create/', views.review_create, name='review_create'),
    path('edit/<int:pk>/', views.review_update, name='review_update'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),
]
