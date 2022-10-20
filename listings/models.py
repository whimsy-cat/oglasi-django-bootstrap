from django.db import models

from category.models import Category


class Listing(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250, null=False)
    zipcode = models.CharField(max_length=20)
    rooms = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    baths = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    size = models.IntegerField(null=False)
    year_built = models.IntegerField()
    date_listed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ListingAmenities(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)


class ListingFloorPlan(models.Model):
    floor_2d = models.ImageField(upload_to="photos/floor2d")
    floor_3d = models.ImageField(upload_to="photos/floo3rd")
