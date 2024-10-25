from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'address', 'phone', 'website', 'is_open')
    search_fields = ('name', 'address', 'phone', 'website')

admin.site.register(Restaurant, RestaurantAdmin)