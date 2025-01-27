from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def add_or_remove_cart(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart
    next_url = request.GET.get('next', reverse_lazy('shop:products-list'))
    return redirect(next_url)


def add_or_remove_wishlist(request, pk):
    wishlist = request.session.get('wishlist', [])
    if pk in wishlist:
        wishlist.remove(pk)
    else:
        wishlist.append(pk)

    next_url = request.GET.get('next', reverse_lazy('shop:products-list'))
    request.session['wishlist'] = wishlist
    return redirect(next_url)
