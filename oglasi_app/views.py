from django.shortcuts import render
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap, ListingFavorites



def home(request):
    listings = Listing.objects.all().order_by('?')[:8]
    context = {
        'listings': listings
    }
    return render(request, 'home.html', context)
