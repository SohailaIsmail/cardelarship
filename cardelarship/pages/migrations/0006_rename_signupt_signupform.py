# Generated by Django 4.0.3 on 2022-05-23 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_signup_signupt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signupT',
            new_name='signupform',
        ),
    ]