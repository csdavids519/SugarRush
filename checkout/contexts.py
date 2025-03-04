from .models import Basket


def update_basket_total(request):
    """
    Update basket total costs
     - find current basket for user
     - sum all listed product prices with quantity
    """
    if request.user.is_authenticated:
        user = request.user

        basket = Basket.objects.filter(user=user).last()
        basket_products = basket.basket_products.all()
        total_price = sum(
            i.product.price * i.quantity for i in basket_products
            )

        return {'grand_total': total_price}
    return {'grand_total': 0.00}
