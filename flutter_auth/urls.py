from django.urls import path
from . import views

app_name = "flutter_auth"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('customization/', views.user_customization, name='user_customization'),
    path('csrf_token/', views.get_csrf_token, name='csrf_token'),
]
