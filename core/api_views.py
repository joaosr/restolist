from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import authentication
from rest_framework import exceptions


from core.serializers import RestaurantSerializer
from core.models import Restaurant

class RestaurantsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('category',)
    search_fields = ('name', 'description', 'category', 'address')
    pagination_class = RestaurantsPagination

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        return queryset

class RestaurantRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Restaurant.objects.all()
    lookup_field = 'id'
    serializer_class = RestaurantSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            restaurant = response.data
            cache.set('restaurant_data_{}'.format(restaurant['id']), restaurant)
        return response
