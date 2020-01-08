from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from core.serializers import RestaurantSerializer
from core.models import Restaurant

class RestaurantsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id',)
    search_fields = ('name', 'description')
    pagination_class = RestaurantsPagination

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        return queryset
