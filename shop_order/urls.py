from django.urls import path
from . import views

app_name = 'order'


urlpatterns = [
    path('order/detail/<int:id>/', views.order_detail, name='detail'),
    path('order/create/', views.create_order, name='create'),
    path('coupon/<int:id>/', views.coupon_order, name='coupon'),
    path('request/<int:price>/<int:order_id>/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
    path('order/request/', views.send_request1, name='request1'),
    path('order/verify/', views.verify1 , name='verify1'),
]