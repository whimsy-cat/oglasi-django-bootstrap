from django.shortcuts import render


def listings(request):
    return render(request, 'listings.html')


def listing(request, slug):
    print(slug)
    return render(request, 'listing/listing_profile.html')


def create(request):
    return render(request, 'listing/create_new_listing.html')
