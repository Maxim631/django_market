# Generated by Django 4.1.5 on 2023-01-14 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_remove_order_user_alter_order_order_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info_product',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 14, 19, 26, 6, 135143)),
        ),
    ]