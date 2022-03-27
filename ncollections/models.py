from django.conf import settings
from django.db import models
from django.urls import reverse
from .utils import slugify_instance_title
from django.db.models.signals import pre_save, post_save


class Ncollection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=False, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    website = models.CharField(max_length=220, blank=True, null=True)
    featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    social_links = models.TextField(blank=True, null=True)
    volume = models.BigIntegerField(blank=True, null=True)
    weekly_volume = models.IntegerField(blank=True, null=True)
    #image = models.ImageField(upload_to=collection_image_upload_handler, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("ncollections:detail", kwargs={"id": self.id})
    
    def get_single_collection_url(self):
        return reverse("ncollections:single-collection", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse("ncollections:update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("ncollections:delete", kwargs={"id": self.id})

    def get_nft_children(self):
        return self.nnft_set.all()

    def get_nft_create_url(self):
        kwargs = {
            "parent_id": self.id,
        }
        return reverse("ncollections:nft-create", kwargs=kwargs)

def collection_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(collection_pre_save, sender=Ncollection)

def collection_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
        instance.save()

post_save.connect(collection_post_save, sender=Ncollection)  

class Nnft(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collection = models.ForeignKey("Ncollection", on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    rarity = models.CharField(max_length=50, blank=True, null=True)
    link_to_buy = models.TextField(blank=True, null=True)
    attributes = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to=nft_image_upload_handler, blank=True, null=True)

    def get_absolute_url(self):
        return self.collection.get_absolute_url()  # This should probably be changed to a view with parent collection and brother nfts

    def get_hx_url(self):
        kwargs = {
            "parent_id": self.collection.id,
            "id": self.id
        }
        return reverse("ncollections:hx-nft-detail", kwargs=kwargs)

    def get_detail_url(self):
        kwargs = {
            "parent_id": self.collection.id,
            "id": self.id
        }
        return reverse("ncollections:nft-detail", kwargs=kwargs)

    def get_delete_url(self):
        kwargs = {
            "parent_id": self.collection.id,
            "id": self.id
        }
        return reverse("ncollections:nft-delete", kwargs=kwargs)

    def get_edit_url(self):
        kwargs = {
            "parent_id": self.collection.id,
            "id": self.id
        }
        return reverse("ncollections:nft-update", kwargs=kwargs)

    def get_attribute_children(self):
        return self.nattribute_set.all()

    def get_nft_create_url(self):
        kwargs = {
            "parent_id": self.collection.id,
        }
        return reverse("ncollections:nft-create", kwargs=kwargs)

class Nattribute(models.Model):
    nft = models.ForeignKey("Nnft", on_delete=models.CASCADE)
    category = models.CharField(max_length=220)
    name = models.CharField(max_length=220)

    def get_absolute_url(self):
        return self.nnft.get_absolute_url()

    def get_delete_url(self):
        kwargs = {
            "collection_id": self.nft.collection.id,
            "parent_id": self.nft.id,
            "id": self.id
        }
        return reverse("ncollections:attribute-delete", kwargs=kwargs)

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.nft.id,
            "id": self.id
        }
        return reverse("ncollections:hx-attribute-detail", kwargs=kwargs)
        
    