# urls.py
from django.contrib import admin
from django.urls import path, include
from restaurants.views import RestaurantListView
from admin_dashboard.views import (
    admin_dashboard_restaurant_list,
    admin_dashboard_restaurant_create,
    admin_dashboard_restaurant_update,
    admin_dashboard_restaurant_delete,
    admin_dashboard_restaurant_batch_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('auth/', include('authentication.urls')),  # Include authentication URLs
    path('adminDashboard/restaurants/', admin_dashboard_restaurant_list, name='admin_dashboard_restaurant_list'),
    path('adminDashboard/restaurants/add/', admin_dashboard_restaurant_create, name='admin_dashboard_restaurant_create'),
    path('adminDashboard/restaurants/update/<int:pk>/', admin_dashboard_restaurant_update, name='admin_dashboard_restaurant_update'),
    path('adminDashboard/restaurants/delete/<int:pk>/', admin_dashboard_restaurant_delete, name='admin_dashboard_restaurant_delete'),
    path('adminDashboard/delete/', admin_dashboard_restaurant_batch_delete, name='admin_dashboard_restaurant_batch_delete'),
]