# Generated by Django 4.0.3 on 2022-05-25 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feed',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
