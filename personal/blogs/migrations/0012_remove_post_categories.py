# Generated by Django 2.2.1 on 2019-07-09 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20190709_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]
