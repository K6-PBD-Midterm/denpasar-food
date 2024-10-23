"""
URL configuration for denpasar_food project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurants.views import RestaurantListView
from admin_dashboard.views import admin_dashboard_restaurant_list, admin_dashboard_restaurant_create, admin_dashboard_restaurant_update, admin_dashboard_restaurant_delete, admin_dashboard_restaurant_batch_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('', include('authentication.urls')),
    # Add other URL patterns as needed
    path('adminDashboard/restaurants/', admin_dashboard_restaurant_list, name='admin_dashboard_restaurant_list'),
    path('adminDashboard/restaurants/add/', admin_dashboard_restaurant_create, name='admin_dashboard_restaurant_create'),
    path('adminDashboard/restaurants/update/<int:pk>/', admin_dashboard_restaurant_update, name='admin_dashboard_restaurant_update'),
    path('adminDashboard/restaurants/delete/<int:pk>/', admin_dashboard_restaurant_delete, name='admin_dashboard_restaurant_delete'),
    
    # Batch delete path
    path('adminDashboard/delete/', admin_dashboard_restaurant_batch_delete, name='admin_dashboard_restaurant_batch_delete'),
    
]