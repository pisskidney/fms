from django.contrib import admin

from models import Website, Image, Theme

admin.site.register(Website)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('type', 'topic', 'thumbnail', 'preview', 'full')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color1', 'color2', 'color3', 'color4', 'color5')


admin.site.register(Image, ImageAdmin)
admin.site.register(Theme, ThemeAdmin)
# Register your models here.
