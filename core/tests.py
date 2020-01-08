from rest_framework.test import APITestCase
from core.models import Restaurant

class RestaurantListTestCase(APITestCase):
    def test_list_products(self):
        restaurants_count = Restaurant.objects.count()
        response = self.client.get('/api/v1/restaurants/')
        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(response.data['count'], restaurants_count)
        self.assertEqual(len(response.data['results']), restaurants_count)
