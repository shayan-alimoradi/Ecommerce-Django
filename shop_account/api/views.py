from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import (
    AllowAny
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import *
from shop_account.models import *
from .serializers import *


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (IsSuperUser,)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(new_data, status=status.HTTP_400_BAD_REQUEST)