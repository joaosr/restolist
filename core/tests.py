from rest_framework.test import APITestCase
from core.models import Restaurant

from django.contrib.auth.models import User

class RestaurantListTestCase(APITestCase):
    def test_list_restaurants(self):
        restaurants_count = Restaurant.objects.count()
        response = self.client.get('/api/v1/restaurants/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], restaurants_count)
        self.assertEqual(len(response.data['results']), restaurants_count)

class RestaurantUpdateTestCase(APITestCase):
    def setUp(self):
        restaurant = Restaurant(name='Restaurant 1',
            description='hipster, vegan',
            address='street 11',
            phone='+49 30 0000001')
        restaurant.save()

    def test_update_restaurants(self):
        user = User(username='admin', password='123456')
        self.client.force_authenticate(user=user)
        restaurant = Restaurant.objects.first()
        response = self.client.patch(
            '/api/v1/restaurants/{}/'.format(restaurant.id),
            {
                'name': 'New Restaurant',
                'description': 'Awesome Restaurant',
                'address': 'street 1000',
            },
            format='json',
        )
        updated = Restaurant.objects.get(id=restaurant.id)
        self.assertEqual(updated.name, 'New Restaurant')

    def test_update_restaurants_not_authenticated(self):
        restaurant = Restaurant.objects.first()
        response = self.client.patch(
            '/api/v1/restaurants/{}/'.format(restaurant.id),
            {
                'name': 'New Restaurant',
                'description': 'Awesome Restaurant',
                'address': 'street 1000',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 403)
