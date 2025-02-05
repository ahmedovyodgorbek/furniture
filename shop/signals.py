from django.db.models.signals import pre_save
from django.dispatch import receiver
from shop.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def handle_product_price(sender, instance, **kwargs):
    # Fetch old instance if it's an update
    old_instance = None
    if instance.pk:
        try:
            old_instance = ProductModel.objects.get(pk=instance.pk)
            print(f"Updating product {instance.pk}")
            print(f"Old Discount Price: {old_instance.discount_price}, New Price: {instance.price}")
        except ProductModel.DoesNotExist:
            pass  # Handle if object no longer exists

    # Common logic for both create and update
    if instance.discount:
        instance.discount_price = instance.price - (instance.price * instance.discount / 100)
    else:
        instance.discount_price = instance.price
