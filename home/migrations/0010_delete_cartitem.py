# Generated by Django 5.1.3 on 2024-12-09 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_cart_products_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]