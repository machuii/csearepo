from django.contrib import admin

# Register your models here.

from .models import song,playlist

admin.site.register(song)

admin.site.register(playlist)

