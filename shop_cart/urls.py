from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.cart_detail, name='detail'),
    path('add/<int:id>/', views.add_cart, name='add'),
    path('delete/<int:id>/', views.remove_cart, name='remove'),
    path('add-to-compare-list/<int:id>/', views.add_to_compare_list, name='compare'),
    path('compare-list/', views.compare_list, name='compare-list'),
    path('add-single/<int:id>/', views.add_single, name='add-sin'),
    path('remove-single/<int:id>/', views.remove_single, name='rem-sin'),
]