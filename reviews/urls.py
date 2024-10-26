from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
]
