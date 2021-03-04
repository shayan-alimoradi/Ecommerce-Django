from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveUpdateDestroyAPIView,
)
from .permissions import *
from .serializers import *
from .models import *


class ProductListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsSuperUser,)


class ProductRetrieveView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    lookup_fields = ('slug', 'pk')
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)