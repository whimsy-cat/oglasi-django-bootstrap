from django.contrib import admin
from .models import Listing, ListingAmenities, Amenity

admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(ListingAmenities)
