from django.db import models

class Drop(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateField(auto_now=False, auto_now_add=True)