# Generated by Django 4.0.3 on 2022-05-24 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='phone_number',
        ),
    ]
