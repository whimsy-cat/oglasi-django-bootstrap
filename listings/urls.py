from django.urls import path
from listings import views, views_dashboard


urlpatterns = [
    path('', views.listings, name="listings"),
    path('pregled/<slug>/', views.listing, name="listing_profile"),

    # TODO: Redefine pages to specific models 
    path('postavi/', views_dashboard.create, name="listing_create", kwargs={'footer': 'create_listing'}),
    path('postavi/sacuvaj', views_dashboard.submit, name="listing_submit"),
    path('moji-oglasi/', views_dashboard.my_listings, name="listing_my_listings"),
    path('sacuvane-pretrage/', views_dashboard.saved_listings, name="listing_saved_listings"),
    path('profil/', views_dashboard.profile, name="listing_profile"),
    path('poruke/', views_dashboard.messages, name="listing_messages"),
    path('omiljeni-oglasi/', views_dashboard.my_favorites, name="listing_my_favorites"),
    path('pregledi/', views_dashboard.my_views, name="listing_my_views"),
    path('pretplate/', views_dashboard.subscription, name="listing_subscription"),
    path('promovisi-oglas/', views_dashboard.promote_listing, name="listing_promote_listing"),
    path('podesavanja/', views_dashboard.settings, name="listing_settings"),
]
