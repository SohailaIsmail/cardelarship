# Generated by Django 4.0.3 on 2022-05-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0013_delete_adminlogin_delete_login_delete_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=70)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
    ]
