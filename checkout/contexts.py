from .models import Basket


def update_basket_total(request):

    # update basket pice total
    basket = Basket.objects.get(basket_id=1)

    basket_products = basket.basket_products.all()
    print(f"Basket ID: {basket.basket_id}")

    total_price = sum(i.product.price * i.quantity for i in basket_products)
    print(f"total price: {total_price}")

    return {'grand_total': total_price}

