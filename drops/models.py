from django.db import models

class Drop(models.Model):
    title = models.TextField()
    description = models.TextField()