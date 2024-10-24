from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from restaurants.models import Restaurant  # Import from the restaurants module
from .forms import RestaurantForm


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_list(request):
    query = request.GET.get('q')
    if query:
        restaurants = Restaurant.objects.filter(name__icontains=query)
    else:
        restaurants = Restaurant.objects.all()
    
    return render(request, 'admin_dashboard_restaurant_list.html', {'restaurants': restaurants})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard_restaurant_list')
    else:
        form = RestaurantForm()

    return render(request, 'restaurant_form.html', {'form': form})  # Adjusted template path

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        # Redirect to admin dashboard restaurant list after deletion
        return redirect('admin_dashboard_restaurant_list')
    return render(request, 'restaurant_confirm_delete.html', {'restaurant': restaurant})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_batch_delete(request):
    if request.method == 'POST':
        restaurant_ids = request.POST.getlist('restaurant_ids')
        Restaurant.objects.filter(id__in=restaurant_ids).delete()
        return redirect('admin_dashboard_restaurant_list')
    
