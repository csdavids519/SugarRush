# Generated by Django 5.1.5 on 2025-07-07 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0014_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='ShippingInfo',
        ),
    ]
