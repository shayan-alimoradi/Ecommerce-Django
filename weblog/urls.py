from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_core.urls', namespace='core')),
    path('', include('shop_product.urls', namespace='product')),
    path('', include('shop_account.urls', namespace='account')),
    path('cart/', include('shop_cart.urls', namespace='cart')),
    path('order/', include('shop_order.urls', namespace='order')),
    path('captcha/', include('captcha.urls')),
]
