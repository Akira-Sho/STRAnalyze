# Generated by Django 2.2.5 on 2021-11-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0025_auto_20211110_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='brand_name',
            field=models.CharField(choices=[('YONEX', 'YONEX'), ('MIZUNO', 'MIZUNO'), ('DUNLOP', 'DUNLOP'), ('GOSEN', 'GOSEN'), ('SRIXON', 'SRIXON')], default=False, max_length=20, verbose_name='ブランド名'),
        ),
    ]