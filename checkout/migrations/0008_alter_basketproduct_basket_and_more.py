# Generated by Django 5.1.5 on 2025-02-19 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_basketproduct_basket'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketproduct',
            name='basket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket_products', to='checkout.basket'),
        ),
        migrations.AlterField(
            model_name='basketproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in_basket', to='products.product'),
        ),
    ]
