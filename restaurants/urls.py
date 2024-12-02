# urls.py
from django.urls import path
from .views import RestaurantListView, restaurant_list_ajax ,restaurant_list_json, restaurant_detail_json

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('ajax/', restaurant_list_ajax, name='restaurant_list_ajax'),
    path('json/', restaurant_list_json, name='restaurant_list_json'),
    path('json/<int:id>/', restaurant_detail_json, name='restaurant_detail_json'),  # New URL pattern for JSON response by ID

    # Other URL patterns
]