from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Restaurant
from .views import RestaurantListView
from .forms import RestaurantFilterForm
class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            id=123456,
            name="Test Restaurant",
            latitude=12.34,
            longitude=56.78,
            email="test@example.com",
            phone="1234567890",
            website="http://example.com",
            image_url="http://example.com/image.jpg",
            cuisines = ["Asian", "Barbecue"]
        )

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(self.restaurant.email, "test@example.com")
        self.assertEqual(self.restaurant.image_url, "http://example.com/image.jpg")


class RestaurantListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('restaurant_list')
        Restaurant.objects.create(
            id=123457,
            name="Restaurant 1",
            latitude=12.34,
            longitude=56.78,
            email="restaurant1@example.com",
            phone="1234567890",
            website="http://restaurant1.com",
            image_url="http://restaurant1.com/image.jpg",
            cuisines = ["Asian", "Barbecue"],
        )
        Restaurant.objects.create(
            id=123458,
            name="Restaurant 2",
            latitude=12.34,
            longitude=56.78,
            email="restaurant2@example.com",
            phone="0987654321",
            website="http://restaurant2.com",
            image_url="http://restaurant2.com/image.jpg",
            cuisines = ["Asian", "Barbecue"]
        )

    def test_get_context_data(self):
        request = self.factory.get(self.url)
        view = RestaurantListView()
        view.setup(request)
        view.object_list = view.get_queryset()
        context = view.get_context_data()

        self.assertEqual(context['total_restaurants'], 2)
        self.assertIsInstance(context['form'], RestaurantFilterForm)