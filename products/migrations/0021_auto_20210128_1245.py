# Generated by Django 3.1.5 on 2021-01-28 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210128_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product code',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='product_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product screen size',
            new_name='product_screen_size',
        ),
    ]
