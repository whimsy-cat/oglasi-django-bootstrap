from django.db import models

from category.models import Category


class Listing(models.Model):
    name = models.CharField(max_length=150, null=False)
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

    def __str__(self):
        return self.name


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


class ListingDetails(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class ListingAmenities(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)


class ListingFloorPlan(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default=None)
    floor_plan = models.CharField(null=False, max_length=255, default=None)


class ListingImages(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    url = models.CharField(null=False, max_length=255)


class ListingVideo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    url = models.CharField(null=False, max_length=255)


class ListingMap(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    lng = models.DecimalField(decimal_places=2, max_digits=4, null=False)
    zoom = models.IntegerField(null=False)
