from django.contrib import admin
from .models import Property, PropertyImage, Amenity


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


class AmenityInline(admin.TabularInline):
    model = Amenity


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, AmenityInline]


admin.site.register(PropertyImage)
admin.site.register(Amenity)
