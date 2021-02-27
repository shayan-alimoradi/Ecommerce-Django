from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_core.urls', namespace='core')),
    path('', include('shop_product.urls', namespace='product')),
    path('', include('shop_account.urls', namespace='account')),
    path('captcha/', include('captcha.urls')),
]
