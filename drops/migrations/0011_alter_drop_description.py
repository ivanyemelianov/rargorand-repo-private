# Generated by Django 3.2.10 on 2022-03-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0010_alter_drop_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drop',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
