# Generated by Django 3.2.6 on 2021-09-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210901_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID користувача'),
        ),
    ]