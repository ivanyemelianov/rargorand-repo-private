# Generated by Django 3.2.10 on 2022-01-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0004_drop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drop',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
