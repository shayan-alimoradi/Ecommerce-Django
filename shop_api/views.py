from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .pagination import *
from .permissions import *
from .serializers import *
from .models import *


# class ProductListView(ListAPIView):
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     filter_backends = (SearchFilter,)
#     search_fields = ('title',)
#     pagination_class = ProductLimitOffsetPagination

    # def get_queryset(self, *args, **kwargs):
    #     pass


# class ProductCreateView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsSuperUser,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class ProductRetrieveView(RetrieveAPIView):
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     permission_classes = (IsAuthenticated,)


# class ProductUpdateView(UpdateAPIView):
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     lookup_fields = ('pk',)
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class ProductDestroyView(DestroyAPIView):
#     queryset = Product.objects.filter(available=True)
#     serializer_class = ProductSerializer
#     lookup_fields = ('pk',)
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)


# class UserListView(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUser,)


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)
    filterset_fields = ('available',)
    search_fields = ('title',)
    ordering_fields = ('unit_price',)
    # filterset_fields = ('author__username',)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = (IsAuthenticated,)
        else:
            permission_classes = (IsSuperUserOrStaffOrReadOnly,)
        return [permission() for permission in permission_classes]