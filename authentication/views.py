from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Import your custom form
from reviews.models import Review  # Import the Review model
from restaurants.models import Restaurant  # Import the Restaurant model

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('restaurant_list')  # Redirect to the restaurant list page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('authentication:login')  # Redirect to the login page after logout

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use your custom form here
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('authentication:login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Registration failed. Please try a longer password.')
    else:
        form = CustomUserCreationForm()  # Use your custom form here
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def user_customization(request):
    user = request.user
    user_reviews = user.review_set.all()  # Fetch the user's reviews
    liked_restaurants = Restaurant.objects.filter(likes__user=user)  # Restaurants liked by the user

    return render(request, 'authentication/user_customization.html', {
        'user_reviews': user_reviews,
        'liked_restaurants': liked_restaurants,  # Pass the restaurant list to the template
    })
