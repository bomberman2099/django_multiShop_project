# Generated by Django 4.2.6 on 2023-10-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='ادمین'),
        ),
    ]
