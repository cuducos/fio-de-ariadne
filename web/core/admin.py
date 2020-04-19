from django.contrib import admin
from django.utils.safestring import mark_safe

from web.core.models import Kid


class KidModelAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "original",
        "dob",
        "missing_since",
        "eyes",
        "hair",
        "skin",
        "last_seen_at",
        "age_at_occurrence",
    )
    list_filter = (
        "eyes",
        "hair",
        "skin",
        "last_seen_at",
        "age_at_occurrence",
    )

    def original(self, obj):
        label = "Ver link original"
        image = f'<img src="/static/admin/img/icon-viewlink.svg" alt="{label}">'
        return mark_safe(f'<a href="{obj.url}">{image}</a>')


admin.site.register(Kid, KidModelAdmin)
admin.site.site_header = "Ariadne"
admin.site.site_title = "Intranet"
admin.site.index_title = "Fio de Ariadne"
