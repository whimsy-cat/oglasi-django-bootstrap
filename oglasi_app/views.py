from django.shortcuts import render
from category.models import Category
from listings.models import Listing

def home(request):
    listings = Listing.objects.order_by('?')[:24]
    listings1, listings2, listings3 = listings[:8], listings[8:16], listings[16:]
    categories = Category.objects.all()
    total_listings = Listing.objects.count()

    context = {
        'listings1':listings1,
        'listings2': listings2,
        'listings3': listings3,
        'categories': categories,
        'total_listings':total_listings
    }
    return render(request, 'home.html', context)
