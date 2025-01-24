from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import BlogModel, BlogCategoryModel, BlogAuthorModel, BlogCommentModel, BlogTagModel


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


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['description', 'title']
    list_filter = ['title', 'description', 'author', 'categories']


@admin.register(BlogCategoryModel)
class BlogCategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'parent']
    search_fields = ['title']
    list_filter = ['title', 'parent']


@admin.register(BlogAuthorModel)
class BlogAuthorModelAdmin(MyTranslationAdmin):
    list_display = ['first_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']


@admin.register(BlogCommentModel)
class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']


@admin.register(BlogTagModel)
class BlogTagModelAdmin(MyTranslationAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']
