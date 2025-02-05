from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

User = get_user_model()


class ColorModel(BaseModel):
    code = models.CharField(max_length=64, verbose_name=_('code'))
    title = models.CharField(max_length=128, verbose_name=_('name'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductBrandModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('name'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ProductCategoryModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    parent = models.ForeignKey('self', on_delete=models.PROTECT,
                               null=True, blank=True,
                               related_name='children', verbose_name=_('parent')
                               )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductTagModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('tag'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class ProductSizeModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('size'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductModel(BaseModel):
    title = models.CharField(max_length=128, verbose_name=_('title'))
    image1 = models.ImageField(upload_to='products', verbose_name=_('image1'))
    image2 = models.ImageField(upload_to='products', verbose_name=_('image2'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    discount_price = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name=_('discount price'),
                                         null=True, blank=True)
    discount = models.SmallIntegerField(verbose_name=_('discount'), null=True, blank=True)

    description = models.TextField(verbose_name=_('description'))
    sku = models.CharField(max_length=128)
    instock = models.BooleanField(default=True, verbose_name=_('instock'))
    quantity = models.PositiveSmallIntegerField(verbose_name=_('quantity'))

    colors = models.ManyToManyField(ColorModel, verbose_name=_('color'),
                                    related_name='products'
                                    )
    tags = models.ManyToManyField(ProductTagModel, verbose_name=_('tag'),
                                  related_name='products'
                                  )
    sizes = models.ManyToManyField(ProductSizeModel, verbose_name=_('size'),
                                   related_name='products'
                                   )
    categories = models.ManyToManyField(ProductCategoryModel,
                                        related_name='products',
                                        verbose_name=_('categories')
                                        )
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.PROTECT,
                              verbose_name=_('brand'), related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductCommentModel(BaseModel):
    comment = models.CharField(max_length=255, verbose_name=_('comment'))
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name=_('user'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,
                                related_name='comments',
                                verbose_name=_('product'))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class ProductImageModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')
