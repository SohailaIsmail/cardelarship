# Generated by Django 4.0.3 on 2022-05-23 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_signup_alter_login_password_alter_login_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='phone_number',
        ),
    ]