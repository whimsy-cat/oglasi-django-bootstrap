from django.shortcuts import render
from category.models import Category
from listings.models import Listing, Location, PopularLocations
from blog.models import Article

def home(request):
    articles = Article.objects.order_by('-timestamp')[:6]
    listings = Listing.objects.order_by('?')[:24]
    listings1, listings2, listings3 = listings[:8], listings[8:16], listings[16:]
    categories = Category.objects.all()
    total_listings = Listing.objects.count()
    popular_locations = PopularLocations.objects.all()

    all_cities = Location.objects.values('city').distinct()

    context = {
        'listings1':listings1,
        'listings2': listings2,
        'listings3': listings3,
        'categories': categories,
        'total_listings':total_listings,
        'all_cities': all_cities,
        'articles': articles,
        'popular_locations': popular_locations,
    }
    return render(request, 'home.html', context)
