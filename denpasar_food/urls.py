# main_project/urls.py
from django.contrib import admin
from django.urls import path, include
from restaurants.views import RestaurantListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('accounts/', include('authentication.urls')),  # Include authentication URLs
    path('adminDashboard/', include('admin_dashboard.urls', namespace='admin_dashboard')),  # Include admin_dashboard with namespace
]
