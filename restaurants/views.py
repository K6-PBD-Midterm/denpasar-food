# views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Restaurant
from .forms import RestaurantFilterForm
import logging
from django.views.generic import ListView

logger = logging.getLogger(__name__)

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 9

    def get_queryset(self):
        search_by = self.request.GET.get('search_by', 'name')
        search_query = self.request.GET.get('search', '')
        logger.info(f"Search by: {search_by}")
        logger.info(f"Search query: {search_query}")

        queryset = Restaurant.objects.all()

        if search_query:
            filter_kwargs = {f"{search_by}__icontains": search_query}
            queryset = queryset.filter(**filter_kwargs)

        logger.info(f"Queryset count: {queryset.count()}")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_restaurants'] = Restaurant.objects.count()
        context['form'] = RestaurantFilterForm(self.request.GET or None)
        return context

def restaurant_list_ajax(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 9)  # Show 9 restaurants per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'restaurants': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'restaurant_list_ajax.html', context)