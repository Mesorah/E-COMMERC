# Generated by Django 5.1.3 on 2024-12-07 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_products_cover_alter_products_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]
