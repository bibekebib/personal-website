# Generated by Django 2.2.1 on 2019-07-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20190709_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('0', 'blogs'), ('1', 'Technical-writings')], default='blogs', help_text='select category', max_length=255),
        ),
    ]