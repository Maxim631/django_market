# Generated by Django 4.1.5 on 2023-02-04 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_order_order_datetime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 4, 17, 56, 5, 80427)),
        ),
    ]