# Generated by Django 5.1.4 on 2025-01-20 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.IntegerField(verbose_name='code')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='size')),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='ProductTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='tag')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.AddField(
            model_name='productcategorymodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.productcategorymodel', verbose_name='parent'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sku',
            field=models.CharField(default=2024, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productcategorymodel',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(related_name='product_categories', to='shop.productcategorymodel', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image1',
            field=models.ImageField(upload_to='products', verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image2',
            field=models.ImageField(upload_to='products', verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='color',
            field=models.ManyToManyField(related_name='product_colors', to='shop.colormodel', verbose_name='color'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='sizes',
            field=models.ManyToManyField(related_name='product_sizes', to='shop.productsizemodel', verbose_name='size'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='tags',
            field=models.ManyToManyField(related_name='product_tags', to='shop.producttagmodel', verbose_name='color'),
        ),
    ]
