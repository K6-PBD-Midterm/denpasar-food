# admin_dashboard/urls.py
from django.urls import path
from . import views

app_name = 'admin_dashboard'  # Define the namespace

urlpatterns = [
    path('restaurants/', views.admin_dashboard_restaurant_list, name='admin_dashboard_restaurant_list'),
    path('restaurants/add/', views.admin_dashboard_restaurant_create, name='admin_dashboard_restaurant_create'),
    path('restaurants/update/<int:pk>/', views.admin_dashboard_restaurant_update, name='admin_dashboard_restaurant_update'),
    path('restaurants/delete/<int:pk>/', views.admin_dashboard_restaurant_delete, name='admin_dashboard_restaurant_delete'),
    path('delete/', views.admin_dashboard_restaurant_batch_delete, name='admin_dashboard_restaurant_batch_delete'),
]
