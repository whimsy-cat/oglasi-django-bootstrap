from django.db import DataError
from django.shortcuts import render
from django.utils.timezone import now
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingImages, ListingMap


def listings(request):
    return render(request, 'listings.html')


def listing(request, slug):
    print(slug)
    return render(request, 'listing/listing_profile.html')


def create(request, **kwargs):
    details = Detail.objects.all()
    context = {
        'elems': range(0, 30),
        'details': details,
    }
    return render(request, 'listing/create_new_listing.html', context)


def submit(request, args):
    listing_instance = Listing.objects.create(
        name='test',
        description="tester",
        status="buy",
        category=1,
        price=100_000,
        slug="hello_there",
        country="Srbija",
        city="Beograd",
        municipality="Stari Grad",
        area="Dorćol",
        address="Strahinjića Bana",
        date_listed=now()
    )

    ListingCharacteristics.objects.create(
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

    ListingDetails.objects.create(
        listing=listing_instance,
        detail_id=1
    )
    ListingImages.objects.create(
        listing=listing_instance,
        url="https://www.compass.com/m/448c35603c0c966641459a7bfbe9d01a6a54e6a3_img_0_9c76f/1500x1000.jpg"
    )
    ListingMap.objects.create(
        listing=listing_instance,
        lat=44.82,
        lng=20.46,
        zoom=12
    )

    return render(request, "/")
