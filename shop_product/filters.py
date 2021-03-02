import django_filters


class ProductFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name='unit_price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='unit_price', lookup_expr='lte')