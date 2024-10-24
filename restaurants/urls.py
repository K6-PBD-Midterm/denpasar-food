# urls.py
from django.urls import path
from .views import RestaurantListView, restaurant_list_ajax

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('ajax/', restaurant_list_ajax, name='restaurant_list_ajax'),
    # Other URL patterns
]