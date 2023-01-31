from django.contrib import admin
from .models import Listing, CategoryAmenities, ListingAmenities, Amenity, Detail, CategoryDetails, ListingDetails, ListingCharacteristics, ListingMap, ListingFavorites

admin.site.register(Listing)
admin.site.register(ListingCharacteristics)

admin.site.register(Amenity)
admin.site.register(CategoryAmenities)
admin.site.register(ListingAmenities)


admin.site.register(Detail)
admin.site.register(CategoryDetails)

class ListingDetailsAdmin(admin.ModelAdmin):
    list_display = ('listing', 'detail')

admin.site.register(ListingDetails, ListingDetailsAdmin)

admin.site.register(ListingMap)

admin.site.register(ListingFavorites)