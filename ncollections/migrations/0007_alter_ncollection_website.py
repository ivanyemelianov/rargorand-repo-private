# Generated by Django 3.2.10 on 2022-03-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ncollections', '0006_alter_ncollection_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ncollection',
            name='website',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
