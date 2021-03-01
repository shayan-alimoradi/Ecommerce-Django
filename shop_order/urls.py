from django.urls import path
from . import views

app_name = 'order'


urlpatterns = [
    path('detail/<int:id>/', views.order_detail, name='detail'),
    path('create/', views.create_order, name='create'),
    path('coupon/<int:id>/', views.coupon_order, name='coupon'),
]