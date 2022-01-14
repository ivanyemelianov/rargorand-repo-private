from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import slugify_instance_title

class Drop(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
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