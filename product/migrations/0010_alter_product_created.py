# Generated by Django 4.2.6 on 2023-12-15 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_options_remove_product_infotext_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 13, 48, 17, 89059)),
        ),
    ]