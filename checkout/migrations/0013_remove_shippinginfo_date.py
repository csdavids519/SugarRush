# Generated by Django 5.1.5 on 2025-02-20 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0012_shippinginfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippinginfo',
            name='date',
        ),
    ]
