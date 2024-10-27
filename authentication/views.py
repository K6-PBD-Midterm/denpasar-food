# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('authentication:login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Registration failed. Please check your input.')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})

@login_required
def user_customization(request):
    user_reviews = request.user.review_set.all()  
    return render(request, 'authentication/user_customization.html', {'user_reviews': user_reviews})
