from django.db import DataError
from django.shortcuts import render, redirect
from django.utils.timezone import now

from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingImages, ListingMap


def listings(request):
    return render(request, 'listings.html')


def listing(request, slug):
    try:
        listing = Listing.objects.get(slug=slug)
    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing
    }

    return render(request, 'listing/listing_profile.html', context)


def create(request, **kwargs):
    details = Detail.objects.all()
    context = {
        'details': details,
    }
    return render(request, 'listing/create_new_listing.html', context)


def submit(request):
    try:
        listing_category = Category.objects.get(pk=3)
    except Category.DoesNotExist:
        #add error handling
        return redirect('home')

    listing_instance = Listing.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        status=request.POST['status'],
        category=listing_category,
        price=100_000,
        slug="hello_there",
        country="Srbija",
        city="Beograd",
        municipality="Stari Grad",
        area="Dorćol",
        address="Strahinjića Bana",
        date_listed=now()
    )
    listing_instance.save()

    listing_chars = ListingCharacteristics.objects.create(
        listing=listing_instance,
        size=90,
        structure=3.5,
        year_built=1983,
        floor=3,
        total_floors=7,
        bedrooms=3,
        baths=2,
        half_baths=0.5,
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
    listing_images = ListingImages.objects.create(
        listing=listing_instance,
        url="https://www.compass.com/m/448c35603c0c966641459a7bfbe9d01a6a54e6a3_img_0_9c76f/1500x1000.jpg"
    )
    listing_images.save()

    listing_map = ListingMap.objects.create(
        listing=listing_instance,
        lat=44.82,
        lng=20.46,
        zoom=12
    )
    listing_map.save()

    return redirect("home")
