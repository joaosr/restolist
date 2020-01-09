from rest_framework import serializers

from core.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
            model = Restaurant
            fields = (
                'id', 'name', 'description', 'category', 'address', 'phone', 'website'
            )
