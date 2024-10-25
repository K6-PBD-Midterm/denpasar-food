from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from restaurants.models import Restaurant
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
    required_field_names = ['id', 'name', 'latitude', 'longitude', 'cuisines', 'website', 'phone', 'address', 'image_url']
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard:admin_dashboard_restaurant_list')
    else:
        form = RestaurantForm()

    required_fields = [form[field_name] for field_name in required_field_names]
    optional_fields = [form[field_name] for field_name in form.fields if field_name not in required_field_names + ['description']]

    return render(request, 'restaurant_form.html', {
        'form': form,
        'required_fields': required_fields,
        'optional_fields': optional_fields,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_update(request, pk):
    required_field_names = ['id', 'name', 'latitude', 'longitude', 'cuisines', 'website', 'phone', 'address', 'image_url']
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard:admin_dashboard_restaurant_list')
    else:
        form = RestaurantForm(instance=restaurant)

    required_fields = [form[field_name] for field_name in required_field_names]
    optional_fields = [form[field_name] for field_name in form.fields if field_name not in required_field_names + ['description']]

    return render(request, 'restaurant_form.html', {
        'form': form,
        'required_fields': required_fields,
        'optional_fields': optional_fields,
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('admin_dashboard:admin_dashboard_restaurant_list')
    return render(request, 'restaurant_confirm_delete.html', {'restaurant': restaurant})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard_restaurant_batch_delete(request):
    if request.method == 'POST':
        restaurant_ids = request.POST.getlist('restaurant_ids')  # Updated name
        print(f"Form Submitted. IDs received: {restaurant_ids}")  # Debugging line

        if restaurant_ids:
            Restaurant.objects.filter(id__in=restaurant_ids).delete()
            print(f"Deleted Restaurants with IDs: {restaurant_ids}")  # Debugging line

        return redirect('admin_dashboard:admin_dashboard_restaurant_list')



