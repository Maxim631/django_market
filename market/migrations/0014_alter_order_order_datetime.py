# Generated by Django 4.1.5 on 2023-02-04 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_alter_order_order_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 18, 3, 20, 973722)),
        ),
    ]
