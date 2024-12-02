from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Review, Like
from .forms import ReviewForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Restaurant, Review, Like
from .forms import ReviewForm

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
            messages.success(request, 'Your review has been added successfully!')
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
        else:
            messages.error(request, 'There was an error with your review. Please try again.')
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'restaurant': restaurant})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.restaurant_reviews.all()
    user_has_liked = restaurant.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews, 'user_has_liked': user_has_liked})

@login_required
def like_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    like, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant)
    
    if created:
        messages.success(request, f'You have liked {restaurant.name}.')
    else:
        messages.info(request, f'You already liked {restaurant.name}.')
    
    return redirect('restaurant_detail', restaurant_id=restaurant.id)

# New function for restaurant detail JSON response
def restaurant_detail_json(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.restaurant_reviews.all()
    user_has_liked = restaurant.likes.filter(user=request.user).exists() if request.user.is_authenticated else False

    reviews_data = [
        {
            'id': review.id,
            'user': review.user.username,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for review in reviews
    ]

    response_data = {
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'description': restaurant.description,
        },
        'reviews': reviews_data,
        'user_has_liked': user_has_liked,
    }

    return JsonResponse(response_data)

# New function for liking a restaurant JSON response
@login_required
def like_restaurant_json(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    like, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant)

    response_data = {
        'liked': created,
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
        },
        'message': f'You have {"liked" if created else "already liked"} {restaurant.name}.',
    }

    return JsonResponse(response_data)



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
            messages.success(request, 'Your review has been added successfully!')
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
        else:
            messages.error(request, 'There was an error with your review. Please try again.')
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'restaurant': restaurant})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.restaurant_reviews.all()
    user_has_liked = restaurant.likes.filter(user=request.user).exists() if request.user.is_authenticated else False
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews, 'user_has_liked': user_has_liked})

@login_required
def like_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    like, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant)
    if created:
        messages.success(request, f'You have liked {restaurant.name}.')
    else:
        messages.info(request, f'You already liked {restaurant.name}.')
    return redirect('restaurant_detail', restaurant_id=restaurant.id)

# New function for restaurant detail JSON response
def restaurant_detail_json(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.restaurant_reviews.all()
    user_has_liked = restaurant.likes.filter(user=request.user).exists() if request.user.is_authenticated else False

    reviews_data = [
        {
            'id': review.id,
            'user': review.user.username,
            'rating': review.rating,
            'comment': review.comment,
            'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        for review in reviews
    ]

    response_data = {
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'description': restaurant.description,
        },
        'reviews': reviews_data,
        'user_has_liked': user_has_liked,
    }

    return JsonResponse(response_data)

# New function for liking a restaurant JSON response
@login_required
def like_restaurant_json(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    like, created = Like.objects.get_or_create(user=request.user, restaurant=restaurant)

    response_data = {
        'liked': created,
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
        },
        'message': f'You have {"liked" if created else "already liked"} {restaurant.name}.',
    }

    return JsonResponse(response_data)
