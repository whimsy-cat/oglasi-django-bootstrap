from django.urls import path
from blog import views

urlpatterns = [
    path('blog/', views.blog_list, name="blog_list"),
    path('blog/<int:pk>', views.blog_details, name='blog_detail'),

    path('vesti/', views.news_list, name="news_list"),
    path('vesti/<int:pk>', views.news_details, name='news_detail'),
]
