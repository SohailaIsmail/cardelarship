# Generated by Django 4.0.3 on 2022-05-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_remove_signup_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]
