from django.urls import path
from . import views

urlpatterns = [
    path('restaurant/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
]
