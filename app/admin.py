from django.contrib import admin
from .models import Tech, Content, Sticker


class TechAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(Tech, TechAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(Content, ContentAdmin)


class StickerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    search_fields = ('title',)
    list_per_page = 25


admin.site.register(Sticker, StickerAdmin)

