from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel
from shop.models import ProductModel

UserModel = get_user_model()


class OrderModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT,
                             related_name='orders',
                             verbose_name=_('user'))
    status = models.BooleanField(default=False, verbose_name=_('status'))
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('total amount'))
    total_product = models.PositiveSmallIntegerField(verbose_name=_('total product'))

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')


class OrderItem(BaseModel):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items',
                              verbose_name=_('order'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='ordered',
                                verbose_name=_('product'))
    product_title = models.CharField(max_length=128, verbose_name=_('product title'))
    product_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('product price'))
    quantity = models.PositiveSmallIntegerField()



