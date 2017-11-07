from django.contrib import admin

from .models import Artist, Band, Album

admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Album)

