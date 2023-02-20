import random

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap, ListingAmenities, Location
from uploader.models import DropBox
from .helpers import to_type_or_none, pagination_helper


def create(request, **kwargs):
    details = Detail.objects.all()
    categories = Category.objects.all()
    all_cities = Location.objects.values('city').distinct()
    context = {
        'details': details,
        'categories': categories,
        'all_cities': all_cities
    }
    return render(request, 'dashboard_pages/create_new_listing.html', context)


def delete(request, id):
    if request.method == 'POST':
        user = Account.objects.get(id=request.user.id)
        listing = Listing.objects.get(id=id, posted_by=user)
        listing.delete()
        return redirect('listing_my_listings')


def edit(request):
    listing_id = request.POST.get('listing_id')
    user = request.user
    listing = Listing.objects.get(id=listing_id, posted_by=user)
    categories = Category.objects.all()
    context = {
        'listing': listing,
        'categories': categories
    }

    return render(request, 'dashboard_pages/edit_listing.html', context)


def confirm_edit(request, pk):
    user = Account.objects.get(id=request.user.id)
    listing_instance = Listing.objects.get(id=pk, posted_by=user)

    if request.method == 'POST':
        try:
            listing_category = Category.objects.get(pk=request.POST['subcateg'])
        except Category.DoesNotExist:
            # add error handling
            return redirect('home')

        listing_instance.title = request.POST.get('title', listing_instance.title)
        listing_instance.description = request.POST.get('description', listing_instance.description)
        listing_instance.status = request.POST.get('status', listing_instance.status)
        listing_instance.category = listing_category
        listing_instance.price = to_type_or_none(request.POST.get('price'), float, 0.0)
        listing_instance.country = request.POST.get('country', listing_instance.country)
        listing_instance.city = request.POST.get('city', listing_instance.city)
        listing_instance.municipality = request.POST.get('municipality', listing_instance.municipality)
        listing_instance.area = request.POST.get('area', listing_instance.area)
        listing_instance.address = request.POST.get('street', listing_instance.address)
        listing_instance.date_listed = now()


        if request.POST.get('tlocrt[]'):
            prev_floor_plans = listing_instance.floor_plan.all()
            for prev_floor_plan in prev_floor_plans:
                DropBox.objects.get(pk=prev_floor_plan.id).delete()
                listing_instance.floor_plan.remove(prev_floor_plan)

            for floor_plans in request.POST.getlist('tlocrt[]'):
                dropbox = DropBox.objects.get(pk=floor_plans)
                listing_instance.floor_plan.add(dropbox)

        if request.POST.getlist('images[]'):
            prev_images = listing_instance.images.all()
            for prev_img in prev_images:
                DropBox.objects.get(pk=prev_img.id).delete()
                listing_instance.images.remove(prev_img)

            for image in request.POST.getlist('images[]'):
                dropbox = DropBox.objects.get(pk=image)
                listing_instance.images.add(dropbox)


        


        if request.POST.get('video'):
            dropbox = DropBox.objects.get(pk=request.POST['video'])
            listing_instance.video.add(dropbox)

        listing_instance.save()
        
        
        listing_chars, _ = ListingCharacteristics.objects.get_or_create(listing=listing_instance)
        listing_chars.size = to_type_or_none(request.POST['size'], float, 0.0)
        listing_chars.structure = to_type_or_none(request.POST.get('structure'), float, 0.0)
        listing_chars.year_built = to_type_or_none(request.POST.get('year_built'), int)
        listing_chars.floor = to_type_or_none(request.POST.get('floor'), int)
        listing_chars.total_floors = to_type_or_none(request.POST.get('total_floors'), int)
        listing_chars.bedrooms = to_type_or_none(request.POST.get('bedrooms'), int, 0)
        listing_chars.baths = to_type_or_none(request.POST['baths'], int, 0)
        listing_chars.half_baths = to_type_or_none(request.POST['half_baths'], int, 0)
        listing_chars.parking = request.POST.get('parking')
        listing_chars.parking_slots = to_type_or_none(request.POST['baths'], int, 0)
        listing_chars.balcony = to_type_or_none(request.POST['balcony'], int, 0)
        listing_chars.basement = request.POST.get("basement") == "true"
        listing_chars.storage = request.POST.get("storage") == "true"
        listing_chars.legal_status = request.POST.get('legal_status')
        listing_chars.condition = request.POST.get('condition')
        listing_chars.efficiency = request.POST.get('efficiency')
        listing_chars.efficiency_index = request.POST.get('efficiency_index')
        listing_chars.additional = request.POST.get('additional')
        listing_chars.save()

        # Update the listing details
        details_post = request.POST.getlist('details_data')
        ListingDetails.objects.filter(listing=listing_instance).delete()
        for d in details_post:
            listing_details = ListingDetails.objects.create(
                listing=listing_instance,
                detail_id=d
            )
            listing_details.save()

        # Update the listing amenities
        amenities_post = request.POST.getlist('amenities_data')
        ListingAmenities.objects.filter(listing=listing_instance).delete()
        for a in amenities_post:
            listing_amenities = ListingAmenities.objects.create(
                listing=listing_instance,
                amenity_id=a
            )
            listing_amenities.save()


        # Update the listing map
        listing_map = ListingMap.objects.get(listing=listing_instance)
        listing_map.lat = request.POST['lat']
        listing_map.lng = request.POST['lng']
        listing_map.zoom = to_type_or_none(request.POST['zoom'], float, 0.0)
        listing_map.save()


    return redirect('listing_my_listings')



def my_listings(request):
    user = Account.objects.get(id=request.user.id)
    listings = Listing.objects.filter(posted_by=user)
    listings_paginated = pagination_helper(request, listings)

    context = {
        'listings': listings_paginated
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
    listings_paginated = pagination_helper(request, listings, 4)
    context = {
        'listings': listings_paginated
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

    for floor_plans in request.POST.getlist('tlocrt[]'):
        dropbox = DropBox.objects.get(pk=floor_plans)
        listing_instance.floor_plan.add(dropbox)


    for image in request.POST.getlist('images[]'):
        dropbox = DropBox.objects.get(pk=image)
        listing_instance.images.add(dropbox)
        

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
        zoom=to_type_or_none(request.POST['zoom'], float, 0.0),
    )
    listing_map.save()

    return redirect("home")
