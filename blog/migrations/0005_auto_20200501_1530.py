# Generated by Django 3.0.5 on 2020-05-01 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200501_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='like',
            new_name='likes',
        ),
    ]
