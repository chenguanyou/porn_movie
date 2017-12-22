from django.contrib import admin
from huangse import models

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('titles','urls')

# Register your models here.
admin.site.register(models.huangse,PublisherAdmin)