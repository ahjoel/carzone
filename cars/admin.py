from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        if (object.car_photo):
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.car_photo.url))
        else:
            return format_html('<img src="{}" width="40" style="border-radius: 30px;" />'.format(object.car_photo))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')

    list_display_links = ('id', 'thumbnail', 'title',)

    list_editable = ('is_featured',)

    search_fields = ('id', 'title', 'city', 'model', 'body_style', 'fuel_type')

    list_filter = ('city', 'model', 'body_style', 'fuel_type')


admin.site.register(Car, CarAdmin)

