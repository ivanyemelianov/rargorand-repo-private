# Generated by Django 3.2.10 on 2022-03-27 00:51

from django.db import migrations, models
import ncollections.models


class Migration(migrations.Migration):

    dependencies = [
        ('ncollections', '0010_auto_20220323_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='ncollection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ncollections.models.collection_image_upload_handler),
        ),
        migrations.AddField(
            model_name='nnft',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ncollections.models.nft_image_upload_handler),
        ),
    ]
