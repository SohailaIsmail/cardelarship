# Generated by Django 4.0.3 on 2022-05-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_feed_cust_user_feed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='name',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]