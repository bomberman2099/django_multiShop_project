# Generated by Django 4.2.6 on 2023-10-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='colors', to='product.color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100000),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='product.size'),
        ),
    ]
