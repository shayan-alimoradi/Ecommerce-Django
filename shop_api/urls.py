from django.urls import path, include
from . import views

app_name = 'api'


urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('products-create/', views.ProductCreateView.as_view(), name='create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='detail'),
]