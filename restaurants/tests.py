from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Restaurant
from .views import RestaurantListView
from .forms import RestaurantFilterForm

class RestaurantModelTest(TestCase):

    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            osm_id=123456,
            name="Test Restaurant",
            latitude=12.34,
            longitude=56.78,
            amenity="restaurant",
            cuisine="italian",
            city="Test City",
            street="Test Street",
            housenumber="123",
            postcode="12345",
            email="test@example.com",
            phone="1234567890",
            website="http://example.com",
            image_url="http://example.com/image.jpg"
        )

    def test_restaurant_creation(self):
        self.assertEqual(self.restaurant.name, "Test Restaurant")
        self.assertEqual(self.restaurant.cuisine, "italian")
        self.assertEqual(self.restaurant.city, "Test City")
        self.assertEqual(self.restaurant.image_url, "http://example.com/image.jpg")

class RestaurantListViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('restaurant_list')
        Restaurant.objects.create(
            osm_id=123457,
            name="Restaurant 1",
            latitude=12.34,
            longitude=56.78,
            amenity="restaurant",
            cuisine="mexican",
            city="City 1",
            street="Street 1",
            housenumber="123",
            postcode="12345",
            email="restaurant1@example.com",
            phone="1234567890",
            website="http://restaurant1.com",
            image_url="http://restaurant1.com/image.jpg"
        )
        Restaurant.objects.create(
            osm_id=123458,
            name="Restaurant 2",
            latitude=12.34,
            longitude=56.78,
            amenity="restaurant",
            cuisine="chinese",
            city="City 2",
            street="Street 2",
            housenumber="456",
            postcode="67890",
            email="restaurant2@example.com",
            phone="0987654321",
            website="http://restaurant2.com",
            image_url="http://restaurant2.com/image.jpg"
        )

    def test_get_context_data(self):
        request = self.factory.get(self.url)
        view = RestaurantListView()
        view.setup(request)
        view.object_list = view.get_queryset()
        context = view.get_context_data()

        self.assertEqual(context['total_restaurants'], 2)
        self.assertIsInstance(context['form'], RestaurantFilterForm)