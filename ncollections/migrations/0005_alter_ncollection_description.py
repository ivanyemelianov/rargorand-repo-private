# Generated by Django 3.2.10 on 2022-03-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncollections', '0004_auto_20220322_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncollection',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
