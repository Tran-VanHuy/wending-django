from django.contrib import admin
from .models import * 
from django.utils.html import format_html


# Register your models here.
class WeddingEventAdmin(admin.ModelAdmin):
    list_display = ["title", 'order']

class AblumWedingAdmin(admin.ModelAdmin):
    list_display = ["image", 'type']

class BannerAdmin(admin.ModelAdmin):
    list_display = ["_get_thumbnail", "location"]

    def _get_thumbnail(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
    _get_thumbnail.allow_tags = True
    _get_thumbnail.short_description = 'Ảnh banner'

class GuestbookNumberAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "content"]

class DonateAdmin(admin.ModelAdmin):
    list_display = ['title', 'bank', 'account', 'number', 'branch']

admin.site.register(Story)
admin.site.register(WendingPersion)
admin.site.register(WeddingEvent, WeddingEventAdmin)
admin.site.register(AlbumWedding)
admin.site.register(Banner, BannerAdmin)
admin.site.register(GuestbookNumber, GuestbookNumberAdmin)
admin.site.register(Donate, DonateAdmin)






