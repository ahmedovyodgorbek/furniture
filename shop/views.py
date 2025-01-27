from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from . import models
from .models import ProductModel


class ProductsListView(ListView):
    template_name = 'shop/products-list.html'
    model = models.ProductModel
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        products = models.ProductModel.objects.all()
        q = self.request.GET.get('q')
        tag = self.request.GET.get('tag')
        color = self.request.GET.get('color')
        brand = self.request.GET.get('brand')
        size = self.request.GET.get('size')
        cat = self.request.GET.get('cat')
        sort = self.request.GET.get('sort')
        if q:
            products = products.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        if cat:
            products = products.filter(categories=cat)
        if size:
            products = products.filter(sizes=size)
        if tag:
            products = products.filter(tags=tag)
        if color:
            products = products.filter(colors=color)
        if brand:
            products = products.filter(brand=brand)
        if sort:
            products = products.order_by(sort)

        return products

    @staticmethod
    def format_colors():
        colors = models.ColorModel.objects.all()
        result = []
        temp_list = []
        for color in colors:
            temp_list.append(color)
            if len(temp_list) == 2:
                result.append(temp_list)
                temp_list = []
        if len(temp_list) == 1:
            result.append(temp_list)
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sizes'] = models.ProductSizeModel.objects.all()
        context['comments'] = models.ProductCommentModel.objects.all()
        context['brands'] = models.ProductBrandModel.objects.all()
        context['colors'] = self.format_colors()
        context['tags'] = models.ProductTagModel.objects.all()
        context['categories'] = models.ProductCategoryModel.objects.all()

        return context


class ProductDetailView(DetailView):
    model = models.ProductModel
    template_name = 'shop/product-detail.html'
    context_object_name = 'pr'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = self.object

        categories = product.categories.all()

        related_products = ProductModel.objects.filter(categories__in=categories).exclude(id=product.id).distinct()

        context['related_products'] = related_products
        return context


class WishTemplateView(TemplateView):
    template_name = 'shop/user-wishlist.html'


class CartTemplateView(TemplateView):
    template_name = 'shop/product-cart.html'
