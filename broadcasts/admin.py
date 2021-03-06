from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


@admin.register(models.Broadcast)
class BroadcastAdmin(admin.ModelAdmin):

    """Broadcast Admin Definition"""

    list_display = [
        "name",
        "broadcast_host",
        "resolution",
        "on_air",
        "get_thumbnail",
    ]

    list_filter = ("on_air", "genre", "resolution")

    filter_horizontal = ("genre",)

    raw_id_fields = ("broadcast_host",)

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.Genre, models.Resolution)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    pass
