from django.contrib import admin

# Register your models here.

from .models import Album, Song

class AlbumModelAdmin(admin.ModelAdmin):
	list_display = ["album_title", "artist"]
	search_fields = ["album_title", "artist"]
	class Meta:
		model = Album


admin.site.register(Album, AlbumModelAdmin)
admin.site.register(Song)