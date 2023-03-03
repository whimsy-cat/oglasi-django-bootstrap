from django.shortcuts import render
from category.models import Category
from listings.models import Listing, Location
from blog.models import Article
from django.core.mail import send_mail
from oglasi_app import settings

def home(request):
    articles = Article.objects.order_by('-timestamp')[:6]
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
        'all_cities': all_cities,
        'articles': articles
    }
    return render(request, 'home.html', context)
