from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """ A view to return the main shopping page """
    products = Product.objects.all()

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
