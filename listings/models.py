from django.db import models

from category.models import Category


class Listing(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=150, null=False, default="")
    address = models.CharField(max_length=250, null=False)
    zipcode = models.CharField(max_length=20)
    municipality = models.CharField(max_length=250, null=False, default=None)
    city = models.CharField(max_length=150, null=False, default=None)
    rooms = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    baths = models.IntegerField(null=False, default=0)
    half_baths = models.IntegerField(null=False, default=0)
    size = models.IntegerField(null=False)
    year_built = models.IntegerField()
    date_listed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name


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
    floor_2d = models.ImageField(upload_to="photos/floor2d")
    floor_3d = models.ImageField(upload_to="photos/floo3rd")


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

