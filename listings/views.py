import random

from django.db import DataError
from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.utils.timezone import now
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from accounts.models import Account
from category.models import Category
from listings.models import Detail, Listing, ListingCharacteristics, ListingDetails, ListingMap
from uploader.models import DropBox


def listings(request):
    listing_data = Listing.objects.filter(status=0)
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
        listing_images = listing.images.all()

    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing,
        "images": listing_images
    }

    return render(request, 'listing/listing_profile.html', context)


def create(request, **kwargs):
    details = Detail.objects.all()
    categories = Category.objects.all()
    context = {
        'details': details,
        'categories': categories,
    }
    return render(request, 'listing/create_new_listing.html', context)


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
