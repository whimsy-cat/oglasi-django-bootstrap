from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Sort listings
def sort_helper(request, listing_data):
    sort = request.GET.get('sort')
    if sort:
        sort_by_name = sort.split('-')[1]
        sort_by_sign = sort.split('-')[0]
        sort_by_sign = '' if sort_by_sign == 'asc' else '-'
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
    query_city = request.GET.get('grad')
    query_location = request.GET.get('lokacija')
    query_category = request.GET.get('tip')
    query_price = request.GET.get('cena')
    query_size = request.GET.get('povrsina')
    query_structure = request.GET.get('struktura')
    query_details_amenities = request.GET.get('d-a')
    query_type = request.GET.get('search_type')
    query_condition = request.GET.get('condition')
    query_garage = request.GET.get('parking')
    query_total_floors = request.GET.get('spratnost')
    query_grejanje = request.GET.get('grejanje')

    if query_grejanje:
        listing_data = listing_data.filter(
            listingdetails__detail__name=query_grejanje)

    if query_total_floors:
        if query_total_floors == '5':
            listing_data = listing_data.filter(
                listingcharacteristics__total_floors__gte=5)
        else:
            listing_data = listing_data.filter(
                listingcharacteristics__total_floors__iexact=query_total_floors)

    if query_garage:
        listing_data = listing_data.filter(
            listingcharacteristics__parking__iexact=query_garage)

    if query_condition:
        listing_data = listing_data.filter(
            listingcharacteristics__condition__iexact=query_condition)

    if query_type:
        listing_data = listing_data.filter(status__iexact=query_type)

    if query_city:
        listing_data = listing_data.filter(city__iexact=query_city)

    if query_location:
        listing_data = listing_data.filter(area__iexact=query_location)

    if query_category:
        listing_data = listing_data.filter(
            category__name__iexact=query_category)

    if query_price:
        price_range = query_price.split('_')
        start = int(price_range[0]) if price_range[0] else None
        end = int(price_range[1]) if price_range[1] else None
        if start and end:
            listing_data = listing_data.filter(price__range=(start, end))
        elif start:
            listing_data = listing_data.filter(price__gte=start)
        elif end:
            listing_data = listing_data.filter(price__lte=end)

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

    if query_structure:
        if query_structure == '4':
            listing_data = listing_data.filter(
                listingcharacteristics__structure__gte=4)
        else:
            listing_data = listing_data.filter(
                listingcharacteristics__structure__exact=float(query_structure))

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
