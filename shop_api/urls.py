from django.urls import path, include
from . import views

app_name = 'api'


urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductRetrieveView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDestroyView.as_view(), name='destroy'),
]
