from django import template
from inventory.models import *
register = template.Library()


@register.simple_tag()
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return int(qty) * int(unit_price)

@register.simple_tag()
def grandtotal(*args, **kwargs):
    cart = Cart.objects.filter(ischeckout="no")
    total = 0
    for i in cart:
        total+= int(i.productqty) * int(i.productid.price)
    return total

@register.simple_tag()
def totalcart(*args, **kwargs):
    cartcount = Cart.objects.filter(ischeckout="no").count()
    return cartcount


@register.simple_tag()
def remproduct(productid,*args, **kwargs):
    product = Product.objects.get(id=productid)

    try:
        cart = Cart.objects.filter(productid=productid)
        total = 0
        for i in cart:
            total= total + int(i.productqty)
        rem = int(product.stock) - total
    except:
        rem = int(product.stock)
    return rem