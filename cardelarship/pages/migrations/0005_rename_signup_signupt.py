# Generated by Django 4.0.3 on 2022-05-23 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_signup_address_remove_signup_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='signupT',
        ),
    ]