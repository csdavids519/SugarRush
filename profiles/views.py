from django.shortcuts import render
from profiles.models import Customer

# Create your views here.


def profiles(request):
    """ A view to return the index page """

    return render(request, 'profiles.html')


def order_history(request):
    """ A view to return the index page """
    # find the order history based on user name
    try:
        orders = Customer.objects.get(user=request.user)
        print('order_history: basket found')
    except Customer.DoesNotExist:
        print('order_history: basket does not exist')
        return render(request, 'order_history.html', {'order_results': None})
    return render(request, 'order_history.html', {'order_results': orders})
