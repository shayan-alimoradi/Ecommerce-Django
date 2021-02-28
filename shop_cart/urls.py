from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.cart_detail, name='detail'),
    path('add/<int:id>/', views.add_cart, name='add'),
]