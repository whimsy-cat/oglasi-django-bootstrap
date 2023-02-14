from django.db import models

from accounts.models import Account
from category.models import Category
from uploader.models import DropBox
from django.utils.text import slugify


class Listing(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(max_length=1000, null=True)
    status = models.CharField(max_length=25)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=15, null=False)
    slug = models.SlugField(max_length=150, unique=True, default="")
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

    def save(self, *args, **kwargs):
        the_slug = self.city + '-' + self.municipality + \
            '-' + self.area + '-' + self.title
        slug = slugify(the_slug)
        unique_slug = slug
        num = 1
        while Listing.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

    @property
    def likes(self):
        return self.listingfavorites_set.filter(listing=self).values_list('user', flat=True)

    @property
    def details(self):
        return self.listingdetails_set.filter(listing=self).values_list('detail__name', flat=True)

    def __str__(self):
        return self.title


class ListingCharacteristics(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    size = models.DecimalField(decimal_places=2, max_digits=6, null=False)
    structure = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    year_built = models.IntegerField(null=True, default=None)
    floor = models.IntegerField(null=True, default=None)
    total_floors = models.IntegerField(null=True, default=None)
    bedrooms = models.DecimalField(decimal_places=1, max_digits=4, null=False)
    baths = models.IntegerField(null=False, default=0)
    half_baths = models.IntegerField(null=False, default=0)
    parking = models.CharField(null=False, max_length=50)
    parking_slots = models.IntegerField(null=False, default=0)
    balcony = models.IntegerField(null=False, default=0)
    basement = models.BooleanField(null=False, default=False)
    storage = models.BooleanField(null=False, default=False)
    legal_status = models.CharField(null=False, max_length=50)
    condition = models.CharField(null=False, max_length=50)
    efficiency = models.CharField(null=False, max_length=50)
    efficiency_index = models.CharField(null=False, max_length=50)
    additional = models.CharField(default=None, null=False, max_length=50)

    def __str__(self):
        return self.listing.title


class Detail(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    description = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CategoryDetails(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name_plural = "Category Details"


class ListingDetails(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)

    def __str__(self):
        return self.detail.name

    class Meta:
        verbose_name_plural = "Listing Details"


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class CategoryAmenities(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name_plural = "Category Amenities"


class ListingAmenities(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)

    def __str__(self):
        return self.amenity.name

    class Meta:
        verbose_name_plural = "Listing Amenities"


class ListingMap(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    lat = models.DecimalField(decimal_places=6, max_digits=14, null=False)
    lng = models.DecimalField(decimal_places=6, max_digits=14, null=False)
    zoom = models.DecimalField(decimal_places=6, max_digits=14, null=False)

    def __str__(self):
        return self.listing.title

    class Meta:
        verbose_name_plural = "Listing Map"


class ListingFavorites(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + ' - ' + self.listing.title

    class Meta:
        verbose_name_plural = "Favorites"


class Location(models.Model):
    country = models.CharField(max_length=150, null=False, default="Serbia")
    city = models.CharField(max_length=150, null=False, default=None)
    municipality = models.CharField(max_length=250, null=False, default=None)
    area = models.CharField(max_length=250, null=False, default=None)
