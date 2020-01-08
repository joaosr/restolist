from rest_framework import serializers

from core.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
            model = Restaurant
            fields = (
                'id', 'name', 'description', 'address', 'phone', 'website',
                'created_at',
            )
