# Copyright 2013 Christoph Siedentop <digikamweb@siedentop.name>
from django.contrib import admin
from digikam.models import AlbumRoot, Album, Image, Tag, ImageTag

class AlbumAdmin(admin.ModelAdmin):
	list_display = ['id', 'albumroot', 'relativepath', 'date', 'caption', 'collection', 'icon']
admin.site.register(Album, AlbumAdmin)

class AlbumRootAdmin(admin.ModelAdmin):
    list_display = ['id', 'label', 'status', 'type', 'identifier', 'specificpath']
admin.site.register(AlbumRoot, AlbumRootAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'album', 'status', 'category', 'filesize']
admin.site.register(Image, ImageAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'usage_count', 'get_images']
    list_filter = ('name', 'id', 'usage_count')
admin.site.register(Tag, TagAdmin)
