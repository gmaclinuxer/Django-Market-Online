from django.shortcuts import render

# Create your views here.
from cartapp.cart import Cart, CART_ID
from productapp.models import Product

def view_cart(request):
    cart=Cart(request)
    return render(request, 'cartapp/view_cart.html', locals())

def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, quantity)
    #request.session[CART_ID] = cart.id
    return view_cart(request)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return view_cart(request)

def clean_cart(request):
    cart = Cart(request)
    cart.clear()
    return view_cart(request)
