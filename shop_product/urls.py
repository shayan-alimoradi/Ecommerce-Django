from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='list'),
    path('product/<slug:slug>/<int:id>/', views.product_detail, name='detail'),
]