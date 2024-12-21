from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm  # Use built-in UserCreationForm
from restaurants.models import Restaurant

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "success", "message": "Login successful", "username": username})
        else:
            return JsonResponse({"status": "error", "message": "Invalid credentials"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"status": "success", "message": "Logout successful"})

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success", "message": "Registration successful"})
        else:
            return JsonResponse({"status": "error", "message": "Registration failed. Please try a longer password."})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@login_required
@csrf_exempt
def user_customization(request):
    user = request.user
    user_reviews = user.review_set.all()
    liked_restaurants = Restaurant.objects.filter(likes__user=user)

    return JsonResponse({
        "status": "success",
        "user_reviews": list(user_reviews.values()),
        "liked_restaurants": list(liked_restaurants.values())
    })

@csrf_exempt
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})
