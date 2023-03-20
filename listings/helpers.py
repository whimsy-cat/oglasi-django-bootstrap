from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.models import ListingPrice
from django.db.models import Q, Subquery, OuterRef, FloatField 
from django.db.models.functions import Cast


# Sort listings
def sort_helper(request, listing_data):
    sort = request.GET.get('sort')
    if sort:
        sort_by_name = sort.split('-')[1]
        sort_by_sign = sort.split('-')[0]
        sort_by_sign = '' if sort_by_sign == 'asc' else '-'

        if sort_by_name == 'price':
            latest_listing_prices = ListingPrice.objects.filter(listing=OuterRef('pk')).order_by('-timestamp')[:1]
            listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).order_by(sort_by_sign + 'latest_price')
        else:
            listing_data = listing_data.order_by(sort_by_sign + sort_by_name)

    return listing_data


def pagination_helper(request, listing_data, offset=12):
    paginator = Paginator(listing_data, offset)
    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    return listings


# Query listings
def query_params_helper(request, listing_data):
    query_search = request.GET.get('search')

    query_city = request.GET.get('grad')
    query_location = request.GET.get('lokacija')
    query_category = request.GET.get('tip')
    query_structure = request.GET.getlist('struktura')
    query_details_amenities = request.GET.get('d-a')
    query_type = request.GET.get('search_type')
    query_condition = request.GET.get('condition')
    query_garage = request.GET.get('parking')

    query_total_floors = request.GET.get('spratnost')
    min_spratnost = request.GET.get('min_spratnost')
    max_spratnost = request.GET.get('max_spratnost')
    min_spratnost = int(min_spratnost.replace(',', '')) if min_spratnost else None
    max_spratnost = int(max_spratnost.replace(',', '')) if max_spratnost else None

    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    min_price = int(min_price.replace('.', '').replace(',', '')) if min_price else None
    max_price = int(max_price.replace('.', '').replace(',', '')) if max_price else None
    query_price = request.GET.get('cena')

    query_size = request.GET.get('povrsina')
    min_size = request.GET.get('min_size', '')
    max_size = request.GET.get('max_size', '')
    min_size = int(float(min_size.replace(',', ''))) if min_size else None
    max_size = int(float(max_size.replace(',', ''))) if max_size else None

    query_grejanje = request.GET.get('grejanje')
    query_setup = request.GET.get('set-up')
    query_acctype = request.GET.get('acc-type')


    if query_acctype:
        listing_data = listing_data.filter(posted_by__type=query_acctype)
  
    if query_setup:
        listing_data = listing_data.filter(listingcharacteristics__set_up__in=query_setup)

    if query_search:
        listing_data = listing_data.filter(title=query_search)

    if query_grejanje:
        listing_data = listing_data.filter(
            listingdetails__detail__name=query_grejanje)
        
    if query_price:
        latest_listing_prices = ListingPrice.objects.filter(listing=OuterRef('pk')).order_by('-timestamp')[:1]
        price_range = query_price.split('_')
        start = int(price_range[0]) if price_range[0] else None
        end = int(price_range[1]) if price_range[1] else None
        if start and end:
            listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__range=(start, end))
        elif start:
            listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__gte=start)
        elif end:
            listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__lte=end)
    elif min_price and max_price:
        latest_listing_prices = ListingPrice.objects.filter(listing=OuterRef('pk')).order_by('-timestamp')[:1]
        listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__range=(min_price, max_price))
    elif min_price:
        latest_listing_prices = ListingPrice.objects.filter(listing=OuterRef('pk')).order_by('-timestamp')[:1]
        listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__gte=min_price)
    elif max_price:
        latest_listing_prices = ListingPrice.objects.filter(listing=OuterRef('pk')).order_by('-timestamp')[:1]
        listing_data = listing_data.annotate(latest_price=Subquery(latest_listing_prices.values('price'))).filter(latest_price__lte=max_price)

    
    if query_total_floors:
            if query_total_floors == '5':
                listing_data = listing_data.filter(
                    listingcharacteristics__total_floors__gte=5)
            else:
                listing_data = listing_data.filter(
                    listingcharacteristics__total_floors__iexact=query_total_floors)
    elif min_spratnost and max_spratnost:
        listing_data = listing_data.filter(listingcharacteristics__floor__range=(min_spratnost, max_spratnost))
    elif min_spratnost:
        listing_data = listing_data.filter(listingcharacteristics__floor__gte=min_spratnost)
    elif max_spratnost:
        listing_data = listing_data.filter(listingcharacteristics__floor__lte=max_spratnost)

    if query_size:
        size_range = query_size.split('_')
        start = float(size_range[0]) if size_range[0] else None
        end = float(size_range[1]) if size_range[1] else None
        if start and end:
            listing_data = listing_data.filter(
                listingcharacteristics__size__range=(start, end))
        elif start:
            listing_data = listing_data.filter(
                listingcharacteristics__size__gte=start)
        elif end:
            listing_data = listing_data.filter(
                listingcharacteristics__size__lte=end)
    elif min_size and max_size:
        listing_data = listing_data.filter(listingcharacteristics__size__range=(min_size, max_size))
    elif min_size:
        listing_data = listing_data.filter(listingcharacteristics__size__gte=min_size)
    elif max_size:
        listing_data = listing_data.filter(listingcharacteristics__size__lte=max_size)


    if query_garage:
        listing_data = listing_data.filter(
            listingcharacteristics__parking__iexact=query_garage)

    if query_condition:
        listing_data = listing_data.filter(
            listingcharacteristics__condition__iexact=query_condition)

    if query_type:
        listing_data = listing_data.filter(type__iexact=query_type)

    if query_city:
        listing_data = listing_data.filter(city__iexact=query_city)

    if query_location:
        listing_data = listing_data.filter(area__iexact=query_location)

    if query_category:
        listing_data = listing_data.filter(Q(category__name=query_category) | Q(category__parent__name=query_category))
   
    if query_structure:
        if query_structure == '5' or query_structure == 5:
            listing_data = listing_data.annotate(str=Cast('listingcharacteristics__structure', FloatField())).filter(str__gte=5)
        else:
            listing_data = listing_data.filter(listingcharacteristics__structure__in=query_structure)

    if query_details_amenities:
        detailsParam = query_details_amenities.split('_')[0]
        amenitiesParam = query_details_amenities.split('_')[1]
        if detailsParam:
            detailsParamsSplited = detailsParam.split('-')
            for d in detailsParamsSplited:
                listing_data = listing_data.filter(listingdetails__detail=d)
        if amenitiesParam:
            amenitiesParamsSplited = amenitiesParam.split('-')
            for a in amenitiesParamsSplited:
                listing_data = listing_data.filter(listingamenities__amenity=a)

    return listing_data

# Parsers


def to_type_or_none(string, target_type, default=None):
    try:
        return target_type(string)
    except ValueError:
        return default
