# Generated by Django 4.0.3 on 2022-05-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('carmodel', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=12)),
                ('content', models.TextField(max_length=12)),
                ('price', models.DecimalField(decimal_places=3, max_digits=50)),
                ('fuel', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('c_image', models.ImageField(default='images/defaulcar.jpeg', upload_to='photos')),
            ],
        ),
    ]
