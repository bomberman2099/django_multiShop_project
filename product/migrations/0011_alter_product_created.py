# Generated by Django 4.2.6 on 2023-12-15 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 13, 48, 43, 316388)),
        ),
    ]
