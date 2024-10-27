# reviews/tests.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Restaurant, Review, Like


class ReviewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test restaurant with a manually set ID
        self.restaurant = Restaurant.objects.create(
            id=1,  # Manually setting the ID to ensure it's not None
            name='Test Restaurant',
            address='123 Test St',
            phone='123-456-7890',
            price_range='$$'
        )

        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

    def test_add_review_view_get(self):
        # Test the GET request for adding a review
        response = self.client.get(reverse('add_review', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    def test_add_review_view_post(self):
        # Test the POST request for adding a review
        response = self.client.post(reverse('add_review', args=[self.restaurant.id]), {
            'rating': 5,
            'comment': 'Great place!'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful post
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.restaurant, self.restaurant)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, 'Great place!')

    def test_restaurant_detail_view(self):
        # Test the restaurant detail view
        Review.objects.create(
            restaurant=self.restaurant,
            user=self.user,
            rating=4,
            comment='Nice place!'
        )
        response = self.client.get(reverse('restaurant_detail', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_detail.html')
        self.assertContains(response, 'Nice place!')

    def test_like_restaurant_view(self):
        # Test the like restaurant view
        response = self.client.post(reverse('like_restaurant', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after liking
        self.assertEqual(Like.objects.filter(user=self.user, restaurant=self.restaurant).count(), 1)

    def test_dislike_restaurant_view(self):
        # Test the dislike restaurant view
        # First, like the restaurant
        Like.objects.create(user=self.user, restaurant=self.restaurant)
        response = self.client.post(reverse('dislike_restaurant', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect after disliking
        self.assertEqual(Like.objects.filter(user=self.user, restaurant=self.restaurant).count(), 0)
