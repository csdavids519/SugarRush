from .models import Basket
from django.db.models import Sum, F

def update_basket_total(request):

    if request.user.is_authenticated:
        print('UPDATE: USER FOUND')
        user = request.user

        # update basket pice total
        # find current basket
        basket = Basket.objects.filter(user=user).last()
        # get all products in current basket
        basket_products = basket.basket_products.all()
        # sum total cost
        total_price = sum(i.product.price * i.quantity for i in basket_products)

        return {'grand_total': total_price}
    return {'grand_total': 0.00}
