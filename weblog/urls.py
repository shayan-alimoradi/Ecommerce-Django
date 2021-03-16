from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_core.urls', namespace='core')),
    path('', include('shop_product.urls', namespace='product')),
    path('', include('shop_account.urls', namespace='account')),
    path('cart/', include('shop_cart.urls', namespace='cart')),
    path('', include('shop_order.urls', namespace='order')),
    path('', include('shop_contact.urls', namespace='contact')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/products/', include('shop_api.urls', namespace='api')),
    path('api/accounts/', include('shop_account.api.urls', namespace='api-account')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token-auth/', views.obtain_auth_token),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

handler404 = 'shop_product.views.page_not_found'
