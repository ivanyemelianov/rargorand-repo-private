from django.conf import settings
from django.db import models

# Create your models here.
class Ncollection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #website = models.CharField(max_length=220)
    #featured = models.BooleanField(default=False)
    #slug = models.SlugField(unique=True, blank=True, null=True)
    #sociallinks = models.TextField(blank=True, null=True)
    #volume = models.BigIntegerField(blank=True, null=True)
    #weeklyvolume = models.IntegerField(blank=True, null=True)
    #image = models.ImageField(upload_to=collection_image_upload_handler, blank=True, null=True)

class Nnft(models.Model):
    collection = models.ForeignKey("Ncollection", on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #rarity = models.CharField(max_length=50)
    #linktobuy = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to=nft_image_upload_handler, blank=True, null=True)

class Nattribute(models.Model):
    nft = models.ForeignKey("Nnft", on_delete=models.CASCADE)
    category = models.CharField(max_length=220)
    name = models.CharField(max_length=220)