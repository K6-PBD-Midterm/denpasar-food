from django.views.generic import ListView
from restaurants.models import Restaurant
from .forms import RestaurantFilterForm
import logging

logger = logging.getLogger(__name__)

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 10

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