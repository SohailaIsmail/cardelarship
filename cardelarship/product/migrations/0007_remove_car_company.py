# Generated by Django 4.0.3 on 2022-05-26 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_car_fuel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='company',
        ),
    ]
