# Generated by Django 4.2.6 on 2023-10-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_color_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='products'),
        ),
    ]
