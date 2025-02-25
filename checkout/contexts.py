from .models import Basket
from django.db.models import Sum, F

def update_basket_total(request):

    if request.user.is_authenticated:
        print('UPDATE: USER FOUND')
        user = request.user

        # update basket pice total
        basket = Basket.objects.filter(user=user).last()

        basket_products = basket.basket_products.all()
        print('UPDATE: BASKET FOUND')
        print(f"Basket user: {basket.user}")
        print(f"Basket ID: {basket.id}")
        # total_price = basket.basket_products.aggregate(
        #     total=Sum(F('product__price') * F('quantity'))
        #     )['total']
        # print(f"total_price: {total_price}")
        total_price = sum(i.product.price * i.quantity for i in basket_products)
        print('UPDATE: TOTAL')
        print(f"total price: {total_price}")

        return {'grand_total': total_price}
    return {'grand_total': 0.00}
