from django.shortcuts import render


def listings(request):
    return render(request, 'listings.html')
