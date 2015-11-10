from django.contrib import admin

from models import Website, Image, Theme, CSS, ButtonType


class ImageAdmin(admin.ModelAdmin):
    list_display = ('type', 'topic', 'thumbnail', 'preview', 'full')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color1', 'color2', 'color3', 'color4', 'color5')


class WebsiteAdmin(admin.ModelAdmin):
    list_display = (
        'domain_name', 'title', 'owner', 'build_stage', 'button_type', 'domain_type'
    )


class ButtonTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CSSAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'selector', 'rule'
    )


admin.site.register(Website, WebsiteAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(ButtonType, ButtonTypeAdmin)
admin.site.register(CSS, CSSAdmin)
# Register your models here.
