from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def products(request):
    """ A view to return the index page """
    products = Product.objects.all()  # fetch all product data

    context = {
        'products': products,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, product_id=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
