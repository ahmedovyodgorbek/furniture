from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import register, translator, TranslationOptions
from . import models


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@register(models.ProductCategoryModel)
class ProductCategoryModelTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.ColorModel)
class ColorModelTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.ProductModel)
class ProductModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.ProductSizeModel)
class ProductSizeModelTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.ProductTagModel)
class ProductTagModelTranslationOptions(TranslationOptions):
    fields = ('title',)
