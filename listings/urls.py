from django.urls import path
from listings import views


urlpatterns = [
    path('', views.listings, name="listings"),
    path('postavi/', views.create, name="listing_create", kwargs = {'footer': 'create_listing'}),
    path('pregled/<slug>/', views.listing, name="listing_profile"),
]
