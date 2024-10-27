from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Review, Like
from .forms import ReviewForm
from django.http import JsonResponse

@login_required
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'restaurant': restaurant})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.restaurant_reviews.all()

    # Check if the current user has liked the restaurant
    user_has_liked = Like.objects.filter(user=request.user, restaurant=restaurant).exists() if request.user.is_authenticated else False

    # Pass the variables to the template
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'user_has_liked': user_has_liked,
    })

@login_required
def like_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    liked, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant)
    
    if not created:
        # If the like already exists, delete it (toggle behavior)
        liked.delete()
        return JsonResponse({'liked': False})
    
    return JsonResponse({'liked': True})
