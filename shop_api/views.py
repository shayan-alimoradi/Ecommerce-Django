from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)
from shop_account.models import *
from .pagination import *
from .permissions import *
from .serializers import *
from .models import *


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title',)
    pagination_class = ProductLimitOffsetPagination

    # def get_queryset(self, *args, **kwargs):
    #     pass


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUser,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    lookup_fields = ('pk',)
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)