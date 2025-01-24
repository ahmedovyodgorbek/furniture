from modeltranslation.translator import register, translator, TranslationOptions
from . import models


@register(models.BlogCategoryModel)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogTagModel)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.BlogAuthorModel)
class BlogAuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'description')


@register(models.BlogModel)
class BlogAuthorTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
