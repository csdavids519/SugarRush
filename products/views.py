from django.shortcuts import render
from .models import Product

# Create your views here.


def products(request):
    """ A view to return the index page """
    products = Product.objects.all()  # fetch all product data
    return render(request, 'products.html', {'products': products})
