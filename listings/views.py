from django.shortcuts import render


def listings(request):
    return render(request, 'listings.html')


def listing(request, slug):
    print(slug)
    return render(request, 'listing_profile.html')
