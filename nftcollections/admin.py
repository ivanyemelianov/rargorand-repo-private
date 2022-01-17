from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.
from .models import NftCollection, Nft

User = get_user_model()

class NftInline(admin.StackedInline):
    model = Nft
    extra = 0
    #fields = ['name', 'description']

class NftCollectionAdmin(admin.ModelAdmin):
    inlines = [NftInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(NftCollection, NftCollectionAdmin)