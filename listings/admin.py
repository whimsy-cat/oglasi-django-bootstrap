from django.contrib import admin
from .models import Listing, CategoryAmenities, ListingAmenities, Amenity, Detail, CategoryDetails, ListingDetails, ListingCharacteristics, ListingMap

admin.site.register(Listing)
admin.site.register(ListingCharacteristics)

admin.site.register(Amenity)
admin.site.register(CategoryAmenities)
admin.site.register(ListingAmenities)


admin.site.register(Detail)
admin.site.register(CategoryDetails)
admin.site.register(ListingDetails)

admin.site.register(ListingMap)