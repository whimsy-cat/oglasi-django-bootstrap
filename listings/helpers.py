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


# Paginate listings
def pagination_helper(request, listing_data):
    paginator = Paginator(listing_data, 12)
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
