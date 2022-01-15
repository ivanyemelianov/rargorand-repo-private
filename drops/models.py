from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import slugify_instance_title

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

class Drop(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    objects = DropManager()

    def get_absolute_url(self):
        return reverse("drop-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)   

def drop_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(drop_pre_save, sender=Drop)

def drop_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)
        instance.save()

post_save.connect(drop_post_save, sender=Drop)