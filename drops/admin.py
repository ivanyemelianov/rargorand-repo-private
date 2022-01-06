from django.contrib import admin

from .models import Drop

class DropAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'description']

admin.site.register(Drop, DropAdmin)
