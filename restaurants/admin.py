from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'amenity', 'cuisine', 'city', 'image_url')
    search_fields = ('name', 'cuisine', 'city')

admin.site.register(Restaurant, RestaurantAdmin)