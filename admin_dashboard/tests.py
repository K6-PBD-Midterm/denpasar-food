# admin_dashboard/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RestaurantForm, UserForm
from restaurants.models import Restaurant
import json

class AdminDashboardFormsTestCase(TestCase):
    def test_restaurant_form_valid(self):
        form_data = {
            'id': 1,
            'name': 'Test Restaurant',
            'latitude': -8.65,
            'longitude': 115.22,
            'cuisines': json.dumps(['Indonesian', 'Asian']),
            'website': 'https://example.com',
            'phone': '+62 123 4567',
            'address': '123 Test Street',
        }
        form = RestaurantForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_restaurant_form_invalid(self):
        form_data = {
            'id': '',  # Missing required field
            'name': '',
            'latitude': '',
            'longitude': '',
            'cuisines': '',
            'website': '',
            'phone': '',
            'address': '',
        }
        form = RestaurantForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('id', form.errors)
        self.assertIn('name', form.errors)

    def test_user_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123',
            'password_confirm': 'testpass123',
            'is_active': True,
            'is_superuser': False,
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid(self):
        form_data = {
            'username': '',
            'email': '',
            'password': '',
            'password_confirm': '',
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password', form.errors)

    def test_user_form_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpass123',
            'password_confirm': 'differentpass',
            'is_active': True,
            'is_superuser': False,
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password_confirm', form.errors)

    def test_restaurant_form_invalid_cuisines(self):
        form_data = {
            'id': 2,
            'name': 'Invalid Cuisine Restaurant',
            'latitude': -8.70,
            'longitude': 115.25,
            'cuisines': 'Invalid JSON',  # Invalid JSON
            'website': 'https://invalidcuisine.com',
            'phone': '+62 987 6543',
            'address': '456 Invalid Street',
        }
        form = RestaurantForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('cuisines', form.errors)

class AdminDashboardViewsTestCase(TestCase):
    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        # Create a normal user
        self.user = User.objects.create_user('user', 'user@example.com', 'userpass')
        # Create a client
        self.client = Client()
        # Log in as superuser
        self.client.login(username='admin', password='adminpass')
        # Create a restaurant
        self.restaurant = Restaurant.objects.create(
            id=1,
            name='Test Restaurant',
            latitude=-8.65,
            longitude=115.22,
            cuisines=['Indonesian', 'Asian'],
            website='https://example.com',
            phone='+62 123 4567',
            address='123 Test Street',
        )

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard_restaurant_list.html')
        self.assertContains(response, 'Test Restaurant')

    def test_user_list_view(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_dashboard_user_list.html')
        self.assertContains(response, 'admin')
        self.assertContains(response, 'user')

    def test_restaurant_create_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_form.html')

    def test_user_create_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_form.html')

    def test_restaurant_update_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_update', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_form.html')
        self.assertContains(response, 'Test Restaurant')

    def test_user_update_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_update', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_form.html')
        self.assertContains(response, 'user')

    def test_restaurant_delete_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_delete', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurant_confirm_delete.html')
        self.assertContains(response, 'Are you sure you want to delete')

    def test_user_delete_view_get(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_confirm_delete.html')
        self.assertContains(response, 'Are you sure you want to delete')

    def test_restaurant_create_view_post_valid(self):
        form_data = {
            'id': 2,
            'name': 'New Restaurant',
            'latitude': -8.70,
            'longitude': 115.25,
            'cuisines': json.dumps(['European']),
            'website': 'https://newrestaurant.com',
            'phone': '+62 555 6666',
            'address': '789 New Street',
        }
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_restaurant_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Restaurant.objects.filter(name='New Restaurant').exists())

    def test_user_create_view_post_valid(self):
        form_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password_confirm': 'newpass123',
            'is_active': True,
            'is_superuser': False,
        }
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_user_create'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_restaurant_update_view_post_valid(self):
        form_data = {
            'id': self.restaurant.id,
            'name': 'Updated Restaurant',
            'latitude': self.restaurant.latitude,
            'longitude': self.restaurant.longitude,
            'cuisines': json.dumps(self.restaurant.cuisines),
            'website': self.restaurant.website,
            'phone': self.restaurant.phone,
            'address': self.restaurant.address,
        }
        response = self.client.post(
            reverse('admin_dashboard:admin_dashboard_restaurant_update', args=[self.restaurant.id]),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.name, 'Updated Restaurant')

    def test_user_update_view_post_valid(self):
        form_data = {
            'username': 'updateduser',
            'email': self.user.email,
            'is_active': self.user.is_active,
            'is_superuser': self.user.is_superuser,
            'password': '',
            'password_confirm': '',
        }
        response = self.client.post(
            reverse('admin_dashboard:admin_dashboard_user_update', args=[self.user.id]),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_restaurant_delete_view_post(self):
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_restaurant_delete', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Restaurant.objects.filter(id=self.restaurant.id).exists())

    def test_user_delete_view_post(self):
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

    def test_restaurant_batch_delete_view_post(self):
        # Create additional restaurant
        restaurant2 = Restaurant.objects.create(
            id=2,
            name='Second Restaurant',
            latitude=-8.75,
            longitude=115.27,
            cuisines=['French'],
            website='https://secondrestaurant.com',
            phone='+62 777 8888',
            address='456 Second Street'
        )
        data = {'restaurant_ids': [str(self.restaurant.id), str(restaurant2.id)]}
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_restaurant_batch_delete'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Restaurant.objects.filter(id=self.restaurant.id).exists())
        self.assertFalse(Restaurant.objects.filter(id=restaurant2.id).exists())

    def test_user_batch_delete_view_post(self):
        # Create additional user
        user2 = User.objects.create_user('user2', 'user2@example.com', 'userpass2')
        data = {'user_ids': [str(self.user.id), str(user2.id)]}
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_user_batch_delete'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
        self.assertFalse(User.objects.filter(id=user2.id).exists())

    def test_restaurant_list_view_search(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_list'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_list'), {'q': 'Nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Restaurant')

    def test_user_list_view_search(self):
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_list'), {'q': 'admin'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'admin')
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_user_list'), {'q': 'nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'admin')
        self.assertNotContains(response, 'user')

    def test_restaurant_create_view_post_invalid(self):
        form_data = {
            'id': '',
            'name': '',
            'latitude': '',
            'longitude': '',
            'cuisines': '',
            'website': '',
            'phone': '',
            'address': '',
        }
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_restaurant_create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        form = response.context.get('form')
        self.assertFalse(form.is_valid())
        self.assertIn('id', form.errors)
        self.assertIn('name', form.errors)

    def test_user_create_view_post_invalid(self):
        form_data = {
            'username': '',
            'email': '',
            'password': '',
            'password_confirm': '',
        }
        response = self.client.post(reverse('admin_dashboard:admin_dashboard_user_create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        form = response.context.get('form')
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('password', form.errors)

    def test_access_control_normal_user(self):
        # Log in as normal user
        self.client.logout()
        self.client.login(username='user', password='userpass')
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_list'))
        self.assertEqual(response.status_code, 302)  # Redirected to login page
        # Since we cannot modify external modules, we accept the redirect

    def test_access_control_anonymous_user(self):
        # Log out to become anonymous
        self.client.logout()
        response = self.client.get(reverse('admin_dashboard:admin_dashboard_restaurant_list'))
        self.assertEqual(response.status_code, 302)  # Redirected to login page
        # Since we cannot modify external modules, we accept the redirect

