from django.shortcuts import render
from profiles.models import Customer


def profiles(request):
    """ A view to return the index page """

    return render(request, 'profiles.html')


def order_history(request):
    """ A view to return the index page """
    try:
        orders = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return render(request, 'order_history.html', {'order_results': None})
    return render(request, 'order_history.html', {'order_results': orders})
