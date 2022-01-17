from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
"""
- Global
    - NFTs
    - Collections
    - Drops
- User
    - NFTs
    - Collections
        - NFTs
        - Description
    - Drops
"""

class NftCollection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    website = models.CharField(max_length=220)
    featured = models.BooleanField(default=False)
    #sociallinks = 
    #volume =
    #weeklyvolume = 
    #volumelastweek =
    #picture =

    def get_absolute_url(self):
        return reverse("nftcollections:detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("nftcollections:update", kwargs={"id": self.id})

    def get_nfts_children(self):
        return self.nft_set.all()
    

class Nft(models.Model):
    nftcollection = models.ForeignKey("NftCollection", on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    rarity = models.CharField(max_length=50)
    #picture =
    #linktobuy =
    #attributes  (can be another class)

    def get_absolute_url(self):
        return self.nftcollection.get_absolute_url()