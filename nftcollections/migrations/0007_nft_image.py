# Generated by Django 3.2.10 on 2022-02-08 19:19

from django.db import migrations, models
import nftcollections.models


class Migration(migrations.Migration):

    dependencies = [
        ('nftcollections', '0006_nftcollection_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=nftcollections.models.nft_image_upload_handler),
        ),
    ]
