# Generated by Django 3.2.10 on 2022-02-06 22:59

from django.db import migrations, models
import nftcollections.models


class Migration(migrations.Migration):

    dependencies = [
        ('nftcollections', '0005_auto_20220206_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftcollection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=nftcollections.models.collection_image_upload_handler),
        ),
    ]
