# Generated by Django 3.2.7 on 2022-01-16 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20220106_1134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-release_date']},
        ),
    ]
