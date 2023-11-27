from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    
    creator = filters.CharFilter("creator")
    status = filters.CharFilter("status")
    created_at = filters.DateTimeFilter("created_at", lookup_expr='date')
    created_at_after = filters.DateTimeFilter("created_at", lookup_expr='date__gt')
    created_at_before = filters.DateTimeFilter("created_at", lookup_expr='date__lt')
    

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']
