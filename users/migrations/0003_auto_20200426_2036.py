# Generated by Django 3.0.5 on 2020-04-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200426_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/None/no-img.jpg', upload_to='comics/headers/'),
        ),
    ]
