# Generated by Django 2.2.5 on 2021-12-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20211215_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, verbose_name='URL表示名'),
        ),
    ]
