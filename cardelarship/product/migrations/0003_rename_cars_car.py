# Generated by Django 4.0.3 on 2022-05-25 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_cars_c_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
    ]