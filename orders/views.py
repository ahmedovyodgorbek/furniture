from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from shop.models import ProductModel


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


class WishListListView(ListView):
    template_name = 'shop/user-wishlist.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        wishlist = self.request.session.get('wishlist', [])

        products = ProductModel.objects.filter(id__in=wishlist)

        return products


class CartListView(ListView):
    template_name = 'shop/product-cart.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        cart = self.request.session.get('cart', [])

        products = ProductModel.objects.filter(id__in=cart)

        return products
