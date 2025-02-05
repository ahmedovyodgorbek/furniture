from django.contrib import admin

from blogs.admin import MyTranslationAdmin
from . import models


class ProductImageModelAdmin(admin.StackedInline):
    model = models.ProductImageModel


@admin.register(models.ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'price', 'created_at']
    search_fields = ['title', 'price', 'sku']
    list_filter = ['created_at', 'price', 'title', 'categories', 'sizes', 'colors']
    ordering = ['-created_at']
    inlines = [ProductImageModelAdmin]
    readonly_fields = ['discount_price']


@admin.register(models.ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'code']
    search_fields = ['code', 'title']
    list_filter = ['title']


@admin.register(models.ProductCategoryModel)
class ProductCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']


@admin.register(models.ProductTagModel)
class ProductTagModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(models.ProductSizeModel)
class ProductSizeModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['title', 'created_at']


@admin.register(models.ProductCommentModel)
class ProductCommentModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'comment']
    search_fields = ['user__username', 'product__title', 'comment']


@admin.register(models.ProductBrandModel)
class ProductCommentModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']
