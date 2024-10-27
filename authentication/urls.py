from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for login
    path('logout/', views.logout_view, name='logout'),  # URL for logout
    path('register/', views.register_view, name='register'),  # URL for registration
    path('customization/', views.user_customization, name='user_customization'),  # URL for customization
]