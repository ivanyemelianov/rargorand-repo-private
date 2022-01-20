from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models import Q

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

class NftCollectionQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = (
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
        return self.filter(lookups) 

class NftCollectionManager(models.Manager):
    def get_queryset(self):
        return NftCollectionQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


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

    objects = NftCollectionManager()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nftcollections:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("nftcollections:hx-detail", kwargs={"id": self.id})

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

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.nftcollection.id,
            "id": self.id
        }
        return reverse("nftcollections:hx-nft-detail", kwargs=kwargs)