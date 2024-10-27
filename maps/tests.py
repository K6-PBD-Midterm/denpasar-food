from django.test import TestCase, Client
from django.urls import reverse
from restaurants.models import Restaurant

class RestaurantMapViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('map')
        self.restaurant1 = Restaurant.objects.create(
            name="Restaurant 1",
            cuisines="Cuisine 1",
            rating=4.5,
            latitude=-8.65,
            longitude=115.20,
            price_range="$$",
            image_url="http://example.com/image1.jpg"
        )
        self.restaurant2 = Restaurant.objects.create(
            name="Restaurant 2",
            cuisines="Cuisine 2",
            rating=4.0,
            latitude=-8.70,
            longitude=115.25,
            price_range="$$$",
            image_url="http://example.com/image2.jpg"
        )

    def test_url_exists(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'map/map.html')

    def test_returns_all_restaurants(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['restaurants']), 2)

    def test_filters_restaurants_by_name(self):
        response = self.client.get(self.url, {'search': 'Restaurant 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['restaurants']), 1)
        self.assertEqual(response.context['restaurants'][0]['name'], 'Restaurant 1')

   