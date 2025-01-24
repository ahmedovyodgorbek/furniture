from django.contrib import admin

from .models import ContactModel


@admin.register(ContactModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'created_at']
    search_fields = ['subject']
    list_filter = ['created_at']
