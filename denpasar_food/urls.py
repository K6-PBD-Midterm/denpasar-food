from django.contrib import admin
from django.urls import path, include
from restaurants.views import RestaurantListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('auth/', include('authentication.urls')),  
    path('flutter-auth/', include('flutter_auth.urls')), \
    path('admin-dashboard/', include('admin_dashboard.urls', namespace='admin_dashboard')),  # Include admin_dashboard with namespace
    path('reviews/', include('reviews.urls')),
    path('', include('restaurants.urls')),
    path('map/', include('maps.urls')),
]