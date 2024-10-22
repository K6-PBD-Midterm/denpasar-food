from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for login
    path('logout/', views.logout_view, name='logout'),  # URL for logout
    path('register/', views.register_view, name='register'),  # URL for registration
]
