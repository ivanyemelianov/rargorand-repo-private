from django.db import models
from django.utils.text import slugify

class Drop(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)