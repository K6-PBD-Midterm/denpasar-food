from django.db import models
import json

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    reviews_count = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    ranking = models.JSONField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)
    detailed_address = models.JSONField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    reviews_per_rating = models.JSONField(null=True, blank=True)
    review_keywords = models.JSONField(null=True, blank=True)
    is_open = models.BooleanField(null=True, blank=True)
    open_hours = models.JSONField(null=True, blank=True)
    menu_link = models.URLField(null=True, blank=True)
    delivery_url = models.URLField(null=True, blank=True)
    price_range = models.CharField(null=True, blank=True)
    cuisines = models.JSONField(null=True, blank=True)
    diets = models.JSONField(null=True, blank=True)
    meal_types = models.JSONField(null=True, blank=True)
    dining_options = models.JSONField(null=True, blank=True)
    owner_types = models.JSONField(null=True, blank=True)
    top_tags = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name