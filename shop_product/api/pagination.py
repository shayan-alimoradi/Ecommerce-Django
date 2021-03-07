from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)

class CommentListPagination(PageNumberPagination):
    page_size = 3
