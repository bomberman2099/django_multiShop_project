# Generated by Django 4.2.6 on 2023-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_is_active_alter_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=2, max_length=12, unique=True, verbose_name='شماره تلفن'),
            preserve_default=False,
        ),
    ]
