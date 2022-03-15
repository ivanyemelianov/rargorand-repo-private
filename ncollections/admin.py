from django.contrib.auth import get_user_model
from django.contrib import admin

# Register your models here.
from .models import Ncollection, Nnft, Nattribute

User = get_user_model()

class NattributeAdminInline(admin.StackedInline):
    model = Nattribute
    extra = 0

class NnftAdmin(admin.ModelAdmin):
    inlines = [NattributeAdminInline]
    list_display = ['name', 'collection']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['collection']

class NcollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Ncollection, NcollectionAdmin)
admin.site.register(Nnft, NnftAdmin)
