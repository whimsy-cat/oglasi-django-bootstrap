from django.urls import path
from blog import views

urlpatterns = [
    path('', views.article_list, name="blog_list"),
    path('<int:pk>', views.article_detail, name='blog_detail'),
]
