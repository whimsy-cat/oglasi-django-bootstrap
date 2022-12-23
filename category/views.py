from django.shortcuts import render
from rest_framework import viewsets

from category.models import Category
from category.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
