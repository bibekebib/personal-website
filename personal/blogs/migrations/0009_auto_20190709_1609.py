# Generated by Django 2.2.1 on 2019-07-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20190709_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='select author', on_delete=django.db.models.deletion.CASCADE, to='blogs.Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.IntegerField(choices=[(0, 'blogs'), (1, 'Technical-writings')], default=0, help_text='select category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='enter feature image of post', upload_to=''),
        ),
    ]