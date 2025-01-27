from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('wishlist/', views.WishTemplateView.as_view(), name='wishlist'),
    path('cart/', views.CartTemplateView.as_view(), name='cart'),
    path('', views.ProductsListView.as_view(), name='products-list')
]
