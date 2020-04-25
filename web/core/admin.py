from django.contrib import admin
from django.utils.safestring import mark_safe

from web.core.models import Kid


class KidModelAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "original",
        "dob",
        "missing_since",
        "eyes_display",
        "hair_display",
        "skin_display",
        "last_seen_at_city",
        "last_seen_at_state",
        "age_at_occurrence",
    )
    list_filter = (
        "eyes",
        "hair",
        "skin",
        "last_seen_at_city",
        "last_seen_at_state",
        "age_at_occurrence",
    )

    def original(self, obj):
        label = "Ver link original"
        image = f'<img src="/static/admin/img/icon-viewlink.svg" alt="{label}">'
        return mark_safe(f'<a href="{obj.url}">{image}</a>')

    def eyes_display(self, obj):
        return obj.get_eyes_display()

    def hair_display(self, obj):
        return obj.get_hair_display()

    def skin_display(self, obj):
        return obj.get_skin_display()

    eyes_display.short_description = "Cor dos olhos"
    hair_display.short_description = "Cor dos cabelos"
    skin_display.short_description = "Cor da pele"


admin.site.register(Kid, KidModelAdmin)
admin.site.site_header = "Ariadne"
admin.site.site_title = "Intranet"
admin.site.index_title = "Fio de Ariadne"
