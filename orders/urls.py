from django.urls import path

from orders.views import add_or_remove_cart, add_or_remove_wishlist, WishListListView, CartListView, CheckoutFormView

app_name = 'orders'

urlpatterns = [
    path('wishlist/', WishListListView.as_view(), name='wishlist'),
    path('cart/', CartListView.as_view(), name='cart'),
    path('checkout/', CheckoutFormView.as_view(), name='checkout'),
    path('cart/add-or-remove/<int:pk>/', add_or_remove_cart, name='add-or-remove-cart'),
    path('wishlist/add-or-remove/<int:pk>/', add_or_remove_wishlist, name='add-or-remove-wishlist')
]
