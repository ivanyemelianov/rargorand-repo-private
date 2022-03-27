import pathlib
import uuid

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import slugify_instance_title

User = settings.AUTH_USER_MODEL

class DropQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return self.filter(lookups)

class DropManager(models.Manager):
    def get_queryset(self):
        return DropQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

def collection_image_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1()) # uuid1 -> uuid + timestamps
    return f"drops/{new_fname}{fpath.suffix}"

class Drop(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, blank=False, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=120, default=None, blank=True, null=True)
    featured = models.BooleanField(default=False)
    mostanticipated = models.BooleanField(default=False)
    futurefavourite = models.BooleanField(default=False)
    releasedateandtime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=collection_image_upload_handler, blank=True, null=True)

    objects = DropManager()

    @property
    def name(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("drops:detail", kwargs={"id": self.id})

    def get_single_drop_url(self):
        return reverse("drops:single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

    def get_hx_url(self):
        return reverse("drops:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("drops:update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("drops:delete", kwargs={"id": self.id})  

def drop_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(drop_pre_save, sender=Drop)

def drop_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
        instance.save()

post_save.connect(drop_post_save, sender=Drop)