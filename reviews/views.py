from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Make sure users are logged in to review
from .models import Restaurant, Review
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
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'restaurant': restaurant})
