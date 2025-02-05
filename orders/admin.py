from django.contrib import admin
from .models import OrderModel, OrderItem


class OrderItemAdmin(admin.StackedInline):
    list_display = ('order__id', 'product', 'product_title', 'product_price', 'quantity')
    search_fields = ('product_title',)
    list_filter = ('product',)
    model = OrderItem


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    date_hierarchy = 'created_at'
    inlines = [OrderItemAdmin]



