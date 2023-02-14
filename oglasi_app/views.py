from django.shortcuts import render
from category.models import Category
from listings.models import Listing, Location

def home(request):
    listings = Listing.objects.order_by('?')[:24]
    listings1, listings2, listings3 = listings[:8], listings[8:16], listings[16:]
    categories = Category.objects.all()
    total_listings = Listing.objects.count()

    all_cities = Location.objects.values('city').distinct()

    context = {
        'listings1':listings1,
        'listings2': listings2,
        'listings3': listings3,
        'categories': categories,
        'total_listings':total_listings,
        'all_cities': all_cities
    }
    return render(request, 'home.html', context)
