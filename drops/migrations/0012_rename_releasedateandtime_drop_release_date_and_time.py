# Generated by Django 3.2.10 on 2022-03-27 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drops', '0011_alter_drop_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drop',
            old_name='releasedateandtime',
            new_name='release_date_and_time',
        ),
    ]