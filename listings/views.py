from django.shortcuts import render, redirect

from django.http import JsonResponse

from django.db.models.functions import TruncQuarter, Concat, Coalesce
from django.db.models import Avg, F, Value, CharField, Case, When, Q
from django.db import models, connection
import datetime

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, Amenity, CategoryDetails, CategoryAmenities, ListingFavorites, Location, ListingPrice
from blog.models import Article
import json

from .helpers import sort_helper, pagination_helper, query_params_helper


def listings(request):
    listing_data = Listing.objects.all()
    categories = Category.objects.all()
    details = Detail.objects.all()
    amenities = Amenity.objects.all()

    # Query Params
    listing_data = query_params_helper(request, listing_data)

    # Sort Params
    listing_data = sort_helper(request, listing_data)

    # View Query Param
    view = request.GET.get('prikaz')

    locations = Location.objects.all()
    cities = locations.distinct('city')

    # Full Map View
    if view == 'mapa2':
        context = {
            "listings": listing_data,
            "categories": categories,
            "details": details,
            "amenities": amenities,
            "cities": cities
        }
        return render(request, 'listings_fullmap.html', context)
    
    listings = pagination_helper(request, listing_data , 2)

    if view == 'lista':
        context = {
            "listings": listings,
            "categories": categories,
            "details": details,
            "amenities": amenities,
            "cities": cities
        }
        return render(request, 'listings_list_view.html', context)
    
    listings = pagination_helper(request, listing_data, 6)

    if view == 'mreža':
        context = {
            "listings": listings,
            "categories": categories,
            "details": details,
            "amenities": amenities,
            "cities": cities
        }
        return render(request, 'listings_network.html', context)


    # Half Map View
    else:
        # Pagination
        listings = pagination_helper(request, listing_data)

        context = {
            "listings": listings,
            "categories": categories,
            "details": details,
            "amenities": amenities,
            "cities": cities
        }

        return render(request, 'listings.html', context)


def listing(request, slug):
    try:
        listing = Listing.objects.get(slug=slug)

        quarterly_prices = ListingPrice.objects.annotate(
            quarter=TruncQuarter('timestamp')
        ).filter(
            timestamp__gte=datetime.datetime.now() - datetime.timedelta(days=365), listing__city=listing.city
        ).values(
            'quarter'
        ).annotate(
            avg_price=Avg('price')
        ).order_by(
            'quarter'
        )
        
        # TODO: no promoted for now, implement when it comes
        promoted_listings = Listing.objects.all().order_by('?')[:4]
        # TODO: find similar listings based on what?
        similar_listings = Listing.objects.all().order_by('?')[:4]

        articles = Article.objects.all().order_by('-timestamp')[:4]

    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing,
        "promoted_listings": promoted_listings,
        "similar_listings": similar_listings,
        "chart_data": quarterly_prices,
        "articles": articles
    }

    return render(request, 'listing_profile.html', context)


def get_details(request):
    details = CategoryDetails.objects.all()
    amenities = []

    category_id = request.GET.get('category')
    if category_id:
        details = details.filter(category=category_id).values(
            'detail__name', 'detail__id')

    type = request.GET.get('type')
    if type == "1":
        amenities = CategoryAmenities.objects.filter(
            category=category_id).values('amenity__name', 'amenity__id')

    data = {'details': list(details), 'amenities': list(amenities)}
    return JsonResponse(data, safe=False)


def get_subcategories(request):
    category_id = request.GET.get('category')
    categories = Category.objects.filter(
        parent=category_id).values('name', 'id')

    return JsonResponse(list(categories), safe=False)


def add_remove_favorites(request):
    post_data = json.loads(request.body.decode("utf-8"))
    listing = Listing.objects.get(id=post_data['id'])
    user = Account.objects.get(id=request.user.id)

    exists = ListingFavorites.objects.filter(listing=listing, user=user)
    if exists:
        response = False
        ListingFavorites.objects.filter(listing=listing, user=user).delete()
    else:
        response = True
        ListingFavorites.objects.create(listing=listing, user=user)

    return JsonResponse(response, safe=False)


def get_areas(request):
    areas = Location.objects.values('area').filter(city=request.GET.get('city')).distinct()
    municipality = Location.objects.values('municipality').filter(city=request.GET.get('city')).distinct()

    data = {'areas': list(areas),
            'municipality': list(municipality)}

    return JsonResponse(data, safe=False)


def get_areas_distinct(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT area, CASE WHEN municipality <> area THEN CONCAT_WS(' - ', municipality, area) ELSE area END AS area_distinct FROM listings_location WHERE city = %s", [request.GET.get('city')])
        areas = cursor.fetchall()

    data = {'areas': areas}
    return JsonResponse(data, safe=False)