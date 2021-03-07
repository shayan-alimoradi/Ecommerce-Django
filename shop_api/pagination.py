from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)


class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 2