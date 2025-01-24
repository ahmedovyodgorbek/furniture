# Generated by Django 5.1.4 on 2025-01-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_productbrandmodel_productmodel_discount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colormodel',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='colormodel',
            old_name='name_en',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='colormodel',
            old_name='name_uz',
            new_name='title_uz',
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='code',
            field=models.CharField(max_length=64, verbose_name='code'),
        ),
    ]
