# Generated by Django 4.0.3 on 2022-05-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0007_rename_contact_feed_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
    ]
