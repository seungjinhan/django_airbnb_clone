from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Room Type """

    class Meta:
        verbose_name_plural = "Room types"
        ordering = ["created"]


class Amenity(AbstractItem):
    """ Amenity Model """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """ Facility Model """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """ HouseRule Model """

    class Meta:
        verbose_name_plural = "House rules"


class Photo(core_models.TimeStampedModel):
    """ Photo Model """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "rooms.Room", related_name="photos", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField( help_text="How many people will be staying?")
    beds = models.IntegerField()
    baths = models.IntegerField()
    bedrooms = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        "rooms.Roomtype", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity", related_name="rooms", blank=True
    )
    facilities = models.ManyToManyField(
        "rooms.Facility", related_name="rooms", blank=True
    )
    house_rules = models.ManyToManyField(
        "rooms.HouseRule", related_name="rooms", blank=True
    )

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)  # Call the real save() method

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_reviews_len = len(all_reviews)
        if all_reviews_len == 0:
            return 0

        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return round((all_ratings / all_reviews_len), 2)

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url
