import random

from django.shortcuts import render, redirect
from django.utils.timezone import now

from accounts.models import Account
from listings.models import Listing
from .helpers import pagination_helper


def agencies_page(request):
    try:
        listing_data = Listing.objects.all()

        # TODO: no promoted for now, implement when it comes
        promoted_listings = Listing.objects.all().order_by('?')[:6]
        # TODO: find similar listings based on what?
        similar_listings = Listing.objects.all().order_by('?')[:4]

    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing_data,
        "promoted_listings": promoted_listings,
        "similar_listings": similar_listings
    }
    return render(request, 'agencies/agencies_page.html', context )

def about_agency(request):
    user = Account.objects.get(id=request.user.id)
    listings = Listing.objects.filter(posted_by=user)
    listings_paginated = pagination_helper(request, listings, 6)

    context = {
        'listings': listings_paginated
    }
    return render(request, 'agencies/about_agency.html', context)

def investors_page(request):
    try:
        listing_data = Listing.objects.all()

        # TODO: no promoted for now, implement when it comes
        promoted_listings = Listing.objects.all().order_by('?')[:6]
        # TODO: find similar listings based on what?
        similar_listings = Listing.objects.all().order_by('?')[:4]

    except Listing.DoesNotExist:
        # add error handling
        return redirect('home')

    context = {
        "listing": listing_data,
        "promoted_listings": promoted_listings,
        "similar_listings": similar_listings
    }
    return render(request, 'investors/investors_page.html', context )


def about_investor(request):
    user = Account.objects.get(id=request.user.id)
    listings = Listing.objects.filter(posted_by=user)
    listings_paginated = pagination_helper(request, listings, 6)

    context = {
        'listings': listings_paginated
    }
    return render(request, 'investors/about_investor.html', context)


def about_us(request):
    listings1 = Listing.objects.all().order_by('?')[:4]
    listings2 = Listing.objects.all().order_by('?')[:4]
    listings3 = Listing.objects.all().order_by('?')[:4]
    listings4 = Listing.objects.all().order_by('?')[:4]

    context = {
        'listings1': listings1,
        'listings2': listings2,
        'listings3': listings3,
        'listings4': listings4
    }
    return render(request, 'about_us_pages/about_us_carier.html', context)

def news_list(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]

    context = {
        "promoted_listings": promoted_listings,
    }

    return render(request, 'vesti/lista_vesti.html', context)


def open_news(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]

    context = {
        "promoted_listings": promoted_listings,
    }

    return render(request, 'vesti/vesti_page.html', context)


def project_list(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]

    context = {
        "promoted_listings": promoted_listings,
    }

    return render(request, 'project_pages/project_list.html', context)


def project_info(request):
    promoted_listings = Listing.objects.all().order_by('?')[:6]

    context = {
        "promoted_listings": promoted_listings,
    }

    return render(request, 'project_pages/info_about_project.html', context)
