import random

from django.db import DataError
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap, CategoryDetails, CategoryAmenities
from uploader.models import DropBox


def listings(request):
    listing_data = Listing.objects.all()
    categories = Category.objects.all()

    # Query Params
    query_city = request.GET.get('grad')
    query_location = request.GET.get('lokacija')
    query_category = request.GET.get('tip')
    query_price = request.GET.get('cena')
    query_size = request.GET.get('povrsina')
    query_structure = request.GET.get('struktura')
    if query_city:
        listing_data = listing_data.filter(city__iexact=query_city)
    if query_location:
        listing_data = listing_data.filter(area__iexact=query_location)
    if query_category:
        listing_data = listing_data.filter(
            category__name__iexact=query_category)
    if query_price:
        listing_data = listing_data.filter(price__lte=query_price)
    if query_size:
        listing_data = listing_data.filter(
            listingcharacteristics__size__lte=query_size)
    if query_structure:
        listing_data = listing_data.filter(
            listingcharacteristics__structure=query_structure)

    # Sort Params
    sort = request.GET.get('sort')
    if sort:
        sort_by_name = sort.split('-')[1]
        sort_by_sign = sort.split('-')[0]
        sort_by_sign = '' if sort_by_sign == 'asc' else '-'
        listing_data = listing_data.order_by(sort_by_sign + sort_by_name)


    # View Query Param
    view = request.GET.get('prikaz')
    
    # Full Map View
    if view == 'mapa2':
        context = {
            "listings": listing_data,
            "categories": categories,
        }
        return render(request, 'listings_fullmap.html', context)
    
    # Half Map View
    else:
        # Pagination
        paginator = Paginator(listing_data, 12)
        page = request.GET.get('page')

        try:
            listings = paginator.page(page)
        except PageNotAnInteger:
            listings = paginator.page(1)
        except EmptyPage:
            listings = paginator.page(paginator.num_pages)

        context = {
            "listings": listings,
            "categories": categories,
        }

        return render(request, 'listings.html', context)


def listing(request, slug):
    try:
        listing = Listing.objects.get(slug=slug)

        # TODO: no promoted for now, implement when it comes 
        promoted_listings = Listing.objects.all().order_by('?')[:4]
        # TODO: find similar listings based on what?
        similar_listings = Listing.objects.all().order_by('?')[:4]

    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing,
        "promoted_listings": promoted_listings,
        "similar_listings": similar_listings
    }

    return render(request, 'listing_profile.html', context)

def get_details(request):
    details = CategoryDetails.objects.all()
    amenities = []

    category_id = request.GET.get('category')
    if category_id:
        details = details.filter(category=category_id).values('detail__name','detail__id')
    
    status = request.GET.get('status')
    if status == "1":
        amenities = CategoryAmenities.objects.filter(category=category_id).values('amenity__name','amenity__id')

    data = {'details': list(details), 'amenities': list(amenities)}
    return JsonResponse(data, safe=False)

def get_subcategories(request):
    category_id = request.GET.get('category')
    categories = Category.objects.filter(parent=category_id).values('name', 'id')

    return JsonResponse(list(categories), safe=False)

