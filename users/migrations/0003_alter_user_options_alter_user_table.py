# Generated by Django 4.1.5 on 2023-02-04 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
