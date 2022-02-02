import pathlib
import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models import Q
from .utils import slugify_instance_title
from django.db.models.signals import pre_save, post_save

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
    slug = models.SlugField(unique=True, blank=True, null=True)
    #sociallinks = 
    #volume =
    #weeklyvolume = 
    #volumelastweek =
    #image =

    objects = NftCollectionManager()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nftcollections:detail", kwargs={"id": self.id})

    def get_single_collection_url(self):
        return reverse("nftcollections:single-collection", kwargs={"slug": self.slug})

    def get_hx_url(self):
        return reverse("nftcollections:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("nftcollections:update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("nftcollections:delete", kwargs={"id": self.id})

    def get_nfts_children(self):
        return self.nft_set.all()
    

def nft_image_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1()) # uuid1 -> uuid + timestamps
    return f"nftcollections/nft/{new_fname}{fpath.suffix}"

def collection_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(collection_pre_save, sender=NftCollection)

def collection_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
        instance.save()

post_save.connect(collection_post_save, sender=NftCollection)


class NftImage(models.Model):
    nftcollection = models.ForeignKey(NftCollection, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=nft_image_upload_handler) # path/to/the/actual/file.png
    # extracted_text


class Nft(models.Model):
    nftcollection = models.ForeignKey("NftCollection", on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    rarity = models.CharField(max_length=50)
    #linktobuy =
    #attributes  (can be another class)

    def get_absolute_url(self):
        return self.nftcollection.get_absolute_url()

    def get_delete_url(self):
        kwargs = {
            "parent_id": self.nftcollection.id,
            "id": self.id
        }
        return reverse("nftcollections:nft-delete", kwargs=kwargs)

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.nftcollection.id,
            "id": self.id
        }
        return reverse("nftcollections:hx-nft-detail", kwargs=kwargs)