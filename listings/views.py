from django.shortcuts import render

from listings.models import Detail


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

