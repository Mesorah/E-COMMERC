# Generated by Django 5.1.3 on 2024-12-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_remove_ordered_house_number_ordered_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered',
            name='house_number',
            field=models.CharField(default='911', max_length=10),
        ),
    ]