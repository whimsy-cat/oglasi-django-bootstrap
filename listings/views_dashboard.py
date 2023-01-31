import random

from django.db import DataError
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap, ListingFavorites
from uploader.models import DropBox


def create(request, **kwargs):
    details = Detail.objects.all()
    categories = Category.objects.all()
    context = {
        'details': details,
        'categories': categories,
    }
    return render(request, 'dashboard_pages/create_new_listing.html', context)

def my_listings(request):
    user = Account.objects.get(id=request.user.id)
    listings = Listing.objects.filter(posted_by=user)
    context = {
        'listings' : listings
    }
    return render(request, 'dashboard_pages/my_listings.html', context)

def saved_listings(request):
    return render(request, 'dashboard_pages/saved_listings.html')

def messages(request):
    return render(request, 'dashboard_pages/messages.html')

def my_views(request):
    return render(request, 'dashboard_pages/my_views.html')

def my_favorites(request):
    user = Account.objects.get(id=request.user.id)
    listings = Listing.objects.filter(listingfavorites__user=user)
    context = {
        'listings' : listings
    }
    return render(request, 'dashboard_pages/my_favorites.html', context)

def promote_listing(request):
    return render(request, 'dashboard_pages/promote_listing.html')

def profile(request):
    return render(request, 'dashboard_pages/profile.html')
 
def subscription(request):
    return render(request, 'dashboard_pages/subscription.html')

def settings(request):
    return render(request, 'dashboard_pages/settings.html')

def submit(request):
    try:
        listing_category = Category.objects.get(pk=3)
    except Category.DoesNotExist:
        # add error handling
        return redirect('home')

    user = Account.objects.get(id=request.user.id)
    listing_instance = Listing.objects.create(
        posted_by=user,
        title=request.POST['title'],
        description=request.POST['description'],
        status=request.POST['status'],
        category=listing_category,
        price=request.POST['price'],
        slug=slugify(
            request.POST['city'] + '-' +
            request.POST['municipality'] + '-' +
            request.POST['area'] + '-' +
            request.POST['title']
        ),
        country=request.POST['country'],
        city=request.POST['city'],
        municipality=request.POST['municipality'],
        area=request.POST['area'],
        address=request.POST['street'],
        date_listed=now()
    )
    for image in request.POST.getlist('images[]'):
        dropbox = DropBox.objects.get(pk=image)
        listing_instance.images.add(dropbox)

    if request.POST['tlocrt']:
        dropbox = DropBox.objects.get(pk=request.POST['tlocrt'])
        listing_instance.floor_plan.add(dropbox)

    if request.POST['video']:
        dropbox = DropBox.objects.get(pk=request.POST['video'])
        listing_instance.video.add(dropbox)

    listing_instance.save()

    listing_chars = ListingCharacteristics.objects.create(
        listing=listing_instance,
        size=request.POST['size'],
        structure=request.POST['structure'],
        year_built=request.POST['year_built'],
        floor=request.POST['floor'],
        total_floors=request.POST['total_floors'],
        bedrooms=request.POST['bedrooms'],
        baths=request.POST['baths'],
        half_baths=request.POST['half_baths'],
        parking="garaža",
        parking_slots=1,
        balcony="terasa",
        basement=True,
        storage=False,
        legal_status="uknjizen",
        condition="renoviran",
        efficiency="",
        efficiency_index=""
    )
    listing_chars.save()

    listing_details = ListingDetails.objects.create(
        listing=listing_instance,
        detail_id=1
    )
    listing_details.save()

    listing_map = ListingMap.objects.create(
        listing=listing_instance,
        lat=request.POST['lat'],
        lng=request.POST['lng'],
        zoom=request.POST['zoom'],
    )
    listing_map.save()

    return redirect("home")
