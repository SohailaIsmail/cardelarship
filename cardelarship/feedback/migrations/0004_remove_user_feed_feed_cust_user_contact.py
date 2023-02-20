# Generated by Django 4.0.3 on 2022-05-25 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='feed',
        ),
        migrations.AddField(
            model_name='feed',
            name='cust',
            field=models.ForeignKey(default=55, on_delete=django.db.models.deletion.CASCADE, to='feedback.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(default=2, max_length=12),
            preserve_default=False,
        ),
    ]
