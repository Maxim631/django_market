# Generated by Django 4.1.5 on 2023-02-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.IntegerField(null=True),
        ),
    ]
