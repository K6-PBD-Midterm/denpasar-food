from django.urls import path
from maps.views import RestaurantMapView

urlpatterns = [
    path('', RestaurantMapView.as_view(), name='map'),  
   
]
