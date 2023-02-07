from django.shortcuts import render
from category.models import Category
from listings.models import Listing

def home(request):
    listings = Listing.objects.all().order_by('?')[:8]
    categories = Category.objects.all()
    total_listings = Listing.objects.count()

    context = {
        'listings': listings,
        'categories': categories,
        'total_listings':total_listings
    }
    return render(request, 'home.html', context)
