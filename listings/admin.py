from django.contrib import admin
from .models import Listing, CategoryAmenities, ListingAmenities, Amenity, Detail, CategoryDetails, ListingDetails, \
    ListingCharacteristics, ListingMap, ListingFavorites, Location, ListingPrice, PopularLocations


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


class ListingPricesInline(admin.StackedInline):
    model = ListingPrice


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_listed', 'posted_by')
    search_fields = ['title', 'posted_by__email']

    inlines = [
        ListingCharacteristicsInline,
        ListingDetailsInline,
        ListingPricesInline,
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


class LocationAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'municipality', 'area')
    search_fields = ('city', 'municipality', 'area')


admin.site.register(Location, LocationAdmin)


class PopularLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'active')


admin.site.register(PopularLocations, PopularLocationAdmin)
