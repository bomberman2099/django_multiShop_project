# Generated by Django 4.2.6 on 2023-10-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_size_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.size'),
        ),
    ]
