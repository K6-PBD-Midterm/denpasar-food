from django.urls import path
from maps.views import show_map

urlpatterns = [
    path('', show_map, name='map'),  # URL for map
   
]
