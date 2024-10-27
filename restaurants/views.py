# views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Restaurant
from .forms import RestaurantFilterForm
import logging
import random
import json
from itertools import chain

logger = logging.getLogger(__name__)

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        search_by = self.request.GET.get('search_by', 'name')
        selected_cuisines = self.request.GET.getlist('cuisines')

        logger.debug(f"Search: {search}")
        logger.debug(f"Search by: {search_by}")
        logger.debug(f"Selected cuisines: {selected_cuisines}")

        if search:
            if search_by == 'name':
                queryset = queryset.filter(name__icontains=search)
            elif search_by == 'cuisine':
                queryset = queryset.filter(cuisines__icontains=search)

        if selected_cuisines:
            for cuisine in selected_cuisines:
                queryset = queryset.filter(cuisines__icontains=cuisine)

        logger.debug(f"Queryset count after filtering: {queryset.count()}")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_restaurants = list(Restaurant.objects.all())
        featured_restaurants = random.sample(all_restaurants, min(3, len(all_restaurants)))
        context['featured_restaurants'] = featured_restaurants
        context['total_restaurants'] = Restaurant.objects.count()
        context['form'] = RestaurantFilterForm(self.request.GET or None)
        
        # Flatten the list of cuisines
        all_cuisines = Restaurant.objects.values_list('cuisines', flat=True)
        flattened_cuisines = set(chain.from_iterable(all_cuisines))
        context['all_cuisines'] = flattened_cuisines
        
        return context

def restaurant_list_ajax(request):
    return render(request, 'restaurant_list.html', context)