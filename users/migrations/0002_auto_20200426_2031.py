# Generated by Django 3.0.5 on 2020-04-27 03:31

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='images/None/default.jpg', upload_to='profile_pics'),
        ),
    ]
