import random

from django.shortcuts import render, redirect
from django.utils.timezone import now

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap, ListingFavorites, ListingAmenities
from uploader.models import DropBox
from .helpers import to_type_or_none


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
        'listings': listings
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
        'listings': listings
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
        listing_category = Category.objects.get(pk=request.POST['subcateg'])
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
        price=to_type_or_none(request.POST.get('price'), float, 0.0),
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
        size=to_type_or_none(request.POST['size'], float, 0.0),
        structure=to_type_or_none(request.POST.get('structure'), float, 0.0),
        year_built=to_type_or_none(request.POST.get('year_built'), int),
        floor=to_type_or_none(request.POST.get('floor'), int),
        total_floors=to_type_or_none(request.POST.get('total_floors'), int),
        bedrooms=to_type_or_none(request.POST.get('bedrooms'), int, 0),
        baths=to_type_or_none(request.POST['baths'], int, 0),
        half_baths=to_type_or_none(request.POST['half_baths'], int, 0),
        parking=request.POST.get('parking'),
        parking_slots=to_type_or_none(request.POST['baths'], int, 0),
        balcony=to_type_or_none(request.POST['balcony'], int, 0),
        basement=request.POST.get("basement") == "true",
        storage=request.POST.get("storage") == "true",
        legal_status=request.POST.get('legal_status'),
        condition=request.POST.get('condition'),
        efficiency=request.POST.get('efficiency'),
        efficiency_index=request.POST.get('efficiency_index'),
        additional=request.POST.get('additional')
    )
    listing_chars.save()

    # All Details
    details_post = request.POST.getlist('details_data')
    for d in details_post:
        listing_details = ListingDetails.objects.create(
            listing=listing_instance,
            detail_id=d
        )
        listing_details.save()

    # All Amenities
    amenities_post = request.POST.getlist('amenities_data')
    for a in amenities_post:
        listing_amenities = ListingAmenities.objects.create(
            listing=listing_instance,
            amenity_id=a
        )
        listing_amenities.save()

    # Add Map
    listing_map = ListingMap.objects.create(
        listing=listing_instance,
        lat=request.POST['lat'],
        lng=request.POST['lng'],
        zoom=request.POST['zoom'],
    )
    listing_map.save()

    return redirect("home")
