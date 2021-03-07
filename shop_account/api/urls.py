from django.urls import path
from . import views

app_name = 'api-account'


urlpatterns = [
    path('sign-up/', views.UserCreateAPIView.as_view(), name='create'),
    path('sign-in/', views.UserLoginAPIView.as_view(), name='login'),
]