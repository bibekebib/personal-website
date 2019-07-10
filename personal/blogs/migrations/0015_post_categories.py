# Generated by Django 2.2.1 on 2019-07-09 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_remove_post_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ForeignKey(default='', help_text='select category', on_delete=django.db.models.deletion.CASCADE, to='blogs.Categories'),
        ),
    ]
