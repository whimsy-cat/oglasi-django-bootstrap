from django.db import models

from accounts.models import Account
from category.models import Category
from uploader.models import DropBox


class Listing(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    price = models.IntegerField(null=False)
    slug = models.CharField(max_length=150, null=False, default="")
    country = models.CharField(max_length=150, null=False, default="Serbia")
    city = models.CharField(max_length=150, null=False, default=None)
    municipality = models.CharField(max_length=250, null=False, default=None)
    area = models.CharField(max_length=250, null=False, default=None)
    address = models.CharField(max_length=250, null=False)
    date_listed = models.DateTimeField(auto_now_add=True)
    images = models.ManyToManyField(DropBox, related_name="images")
    floor_plan = models.ManyToManyField(DropBox, related_name="floor_plan")
    video = models.ManyToManyField(DropBox, related_name="video")
    posted_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ListingCharacteristics(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    size = models.IntegerField(null=False)
    structure = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    year_built = models.IntegerField(null=True)
    floor = models.IntegerField(null=True)
    total_floors = models.IntegerField(null=True)
    bedrooms = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    baths = models.IntegerField(null=False, default=0)
    half_baths = models.IntegerField(null=False, default=0)
    parking = models.CharField(null=False, max_length=50)
    parking_slots = models.IntegerField(null=False, default=0)
    balcony = models.CharField(null=False, max_length=50)
    basement = models.BooleanField(null=False, default=False)
    storage = models.BooleanField(null=False, default=False)
    legal_status = models.CharField(null=False, max_length=50)
    condition = models.CharField(null=False, max_length=50)
    efficiency = models.CharField(null=False, max_length=50)
    efficiency_index = models.CharField(null=False, max_length=50)


class Detail(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CategoryDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)


class ListingDetails(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class CategoryAmenities(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

class ListingAmenities(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)


class ListingMap(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    lng = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    zoom = models.IntegerField(null=False)

