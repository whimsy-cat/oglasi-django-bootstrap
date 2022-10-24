from django.urls import path
from listings import views


urlpatterns = [
    path('', views.listings, name="listings"),
    path('<slug>/', views.listing, name="listing_profile"),
]
