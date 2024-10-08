import logging
from django.shortcuts import render
from django.views.generic import ListView
from restaurants.models import Restaurant

logger = logging.getLogger(__name__)

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 10

    def get_queryset(self):
        filter_value = self.request.GET.get('filter', 'all')
        logger.info(f"Filter value: {filter_value}")
        
        if filter_value == 'restaurant':
            queryset = Restaurant.objects.filter(amenity='restaurant')
        elif filter_value == 'fast_food':
            queryset = Restaurant.objects.filter(amenity='fast_food')
        else:
            queryset = Restaurant.objects.all()
        
        logger.info(f"Queryset count: {queryset.count()}")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_restaurants'] = Restaurant.objects.count()
        return context


