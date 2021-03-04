from django.urls import path, include
from . import api_views
from . import views

app_name = 'product'


api_urls = [
    path('products/', api_views.ProductListView.as_view()),
    path('products-create/', api_views.ProductCreateView.as_view()),
    path('products/<slug:slug>/<int:pk>/', api_views.ProductRetrieveView.as_view()),
]


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='list'),
    path('category/<slug:slug>/', views.ProductList.as_view(), name='category'),
    path('product/<slug:slug>/<int:id>/', views.product_detail, name='detail'),
    path('add-comment/<int:id>/', views.add_comment, name='comment'),
    path('add-to-favourite/<int:id>/', views.add_favourite, name='fav'),
    path('favourite-list/', views.favourite_list, name='fav-list'),
    path('api/v1/', include(api_urls)),
]