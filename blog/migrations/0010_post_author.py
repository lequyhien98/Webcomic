# Generated by Django 3.0.6 on 2020-06-17 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200616_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Chưa xác định', max_length=250),
        ),
    ]
