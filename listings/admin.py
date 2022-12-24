from django.contrib import admin
from .models import Listing, ListingAmenities, Amenity, Detail, ListingDetails, ListingCharacteristics

admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(ListingAmenities)
admin.site.register(ListingCharacteristics)
admin.site.register(Detail)
admin.site.register(ListingDetails)
