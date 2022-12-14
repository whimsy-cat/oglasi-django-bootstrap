from django.urls import path
from listings import views


urlpatterns = [
    path('/', views.listings, name="listings"),
    path('postavi/', views.create, name="listing_create"),
    path('pregled/<slug>/', views.listing, name="listing_profile"),
]
