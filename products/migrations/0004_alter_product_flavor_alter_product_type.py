# Generated by Django 5.1.5 on 2025-02-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_flavor_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flavor',
            field=models.CharField(blank=True, choices=[('Sour', 'Sour'), ('Sweet', 'Sweet'), ('Fruity', 'Fruity')], max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, choices=[('Sticky', 'Sticky'), ('Hard', 'Hard'), ('Gummy', 'Gummy'), ('Chocolate', 'Chocolate')], max_length=254, null=True),
        ),
    ]
