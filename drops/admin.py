from django.contrib import admin

from .models import Drop

class DropAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'timestamp']
    search_fields = ['title', 'description']
    raw_id_fields = ['user']

admin.site.register(Drop, DropAdmin)
