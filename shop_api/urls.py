from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'


router = routers.SimpleRouter()
router.register('users', views.UserViewSet)
router.register('list', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = [
    # path('list/', views.ProductListView.as_view(), name='list'),
    # path('users/', views.UserListView.as_view(), name='users'),
    # path('create/', views.ProductCreateView.as_view(), name='create'),
    # path('<int:pk>/', views.ProductRetrieveView.as_view(), name='detail'),
    # path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.ProductDestroyView.as_view(), name='destroy'),
    # path('revoke/', views.RevokeToken.as_view(), name='revoke'),
# ]
