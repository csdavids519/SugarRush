from .models import Basket


def update_basket_total(request):

    if request.user.is_authenticated:
        print('contexts: update_basket_total: user authenticated')
        user = request.user

        # update basket pice total
        basket = Basket.objects.filter(user=user).first()

        basket_products = basket.basket_products.all()
        print(f"Basket ID: {basket.user}")

        total_price = sum(i.product.price * i.quantity for i in basket_products)
        print(f"total price: {total_price}")

        return {'grand_total': total_price}
    return {'grand_total': 0.00}
