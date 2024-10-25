from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from restaurants.models import Restaurant
import logging
from django.db.models import Q
import random
import json

#@login_required(login_url='/auth/login')
##def show_map(request):
    ##return render(request, "map/map.html")

class RestaurantMapView(TemplateView):
    model = Restaurant
    template_name = 'map/map.html'
    context_object_name = 'restaurants'


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        search_by = self.request.GET.get('search_by', 'name')

        if search:
            if search_by == 'name':
                queryset = queryset.filter(name__icontains=search)
            elif search_by == 'cuisine':
                queryset = queryset.filter(cuisine__icontains=search)
        else :
            queryset = get_restaurants_in_denpasar()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurants'] = list(Restaurant.objects.values('name', 'cuisines', 'rating', 'latitude', 'longitude','price_range'))
        return context

def restaurant_list_ajax(request):
    search_by = request.GET.get('search_by', 'name')
    search_query = request.GET.get('search', '')
    queryset = Restaurant.objects.all()

    if search_query:
        filter_kwargs = {f"{search_by}__icontains": search_query}
        queryset = queryset.filter(**filter_kwargs)
    context = {
        'restaurants': queryset,
    }
    return render(request, 'map/map.html', context)
# Denpasar coordinates
LATITUDE_MIN = -8.75
LATITUDE_MAX = -8.55
LONGITUDE_MIN = 115.15
LONGITUDE_MAX = 115.30

def get_restaurants_in_denpasar():
    restaurants_in_denpasar = Restaurant.objects.filter(
        latitude__gte=LATITUDE_MIN,
        latitude__lte=LATITUDE_MAX,
        longitude__gte=LONGITUDE_MIN,
        longitude__lte=LONGITUDE_MAX
    )
    return restaurants_in_denpasar