# Generated by Django 5.1.5 on 2025-02-20 11:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_rename_basket_orders_orders_basket_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
