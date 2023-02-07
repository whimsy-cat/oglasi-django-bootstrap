from django.contrib import admin
from .models import Listing, CategoryAmenities, ListingAmenities, Amenity, Detail, CategoryDetails, ListingDetails, ListingCharacteristics, ListingMap, ListingFavorites

class ListingMapInline(admin.StackedInline):
    model = ListingMap
    extra = 0
    max_num = 1

class ListingAmenitiesInline(admin.TabularInline):
    model = ListingAmenities

class ListingDetailsInline(admin.TabularInline):
    model = ListingDetails

class ListingCharacteristicsInline(admin.StackedInline):
    model = ListingCharacteristics
    extra = 0
    max_num = 1

class ListingAdmin(admin.ModelAdmin):
    inlines = [
        ListingCharacteristicsInline,
        ListingDetailsInline,
        ListingAmenitiesInline,
        ListingMapInline
    ]
    class Meta:
        model = Listing


admin.site.register(Listing, ListingAdmin)

# Amenities Admin with categories connected
class CategoryAmenitiesInline(admin.TabularInline):
    model = CategoryAmenities
    verbose_name_plural = "Tipovi koji mogu imati ovaj Amenity"

class AmenityAdmin(admin.ModelAdmin):
    inlines = [CategoryAmenitiesInline]

admin.site.register(Amenity, AmenityAdmin)

#  Details Admin with categories connected
class CategoryDetailsInline(admin.TabularInline):
    model = CategoryDetails
    verbose_name_plural = "Tipovi koji mogu imati ovaj Detail"

class DetailAdmin(admin.ModelAdmin):
    inlines = [CategoryDetailsInline]

admin.site.register(Detail, DetailAdmin)


admin.site.register(ListingFavorites)