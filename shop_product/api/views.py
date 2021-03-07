from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from shop_product.models import *
from .serializers import *
from .pagination import *


class CommentListView(ListAPIView):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('comment',)
    pagination_class = CommentListPagination


class CommentDetailView(RetrieveAPIView):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentDetailSerializer
    # lookup_field = ('pk',)