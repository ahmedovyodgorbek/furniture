from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .forms import CheckoutForm
from shop.models import ProductModel
from .models import OrderModel, OrderItem


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
    paginate_by = 1

    def get_queryset(self):
        wishlist = self.request.session.get('wishlist', [])

        products = ProductModel.objects.filter(id__in=wishlist)

        return products


class CartListView(ListView):
    template_name = 'shop/product-cart.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        cart = self.request.session.get('cart', [])

        products = ProductModel.objects.filter(id__in=cart)

        return products


def calculate_price(products):
    total = 0
    for product in products:
        total += product.price
    return total


class CheckoutFormView(LoginRequiredMixin, FormView):
    template_name = 'shop/product-checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('users:account')

    def form_valid(self, form):
        user = self.request.user
        cart = self.request.session.get('cart', [])
        products = ProductModel.objects.filter(id__in=cart)

        if len(products) == 0:
            messages.info(self.request, 'Your cart is empty! ')
            return redirect(reverse_lazy("shop:products-list"))
        else:
            order = OrderModel.objects.create(
                user=user,
                status=False,
                total_amount=calculate_price(products),
                total_product=len(products)
            )
            for product in products:
                OrderItem.objects.create(
                    order=order,
                    quantity=1,
                    product=product,
                    product_title=product.title,
                    product_price=product.price
                )
            # Clear the cart
            self.request.session['cart'] = []
            self.request.session.modified = True
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
