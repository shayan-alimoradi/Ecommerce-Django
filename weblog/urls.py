# Standard library import
from django.contrib import admin
from django.urls import path, include

# 3rd-party impoart
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('secret-admin-panel/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include('shop_core.urls', namespace='core')),
    path('', include('shop_product.urls', namespace='product')),
    path('', include('shop_account.urls', namespace='account')),
    path('cart/', include('shop_cart.urls', namespace='cart')),
    path('', include('shop_order.urls', namespace='order')),
    path('', include('shop_contact.urls', namespace='contact')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token-auth/', views.obtain_auth_token),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

handler404 = 'shop_product.views.page_not_found'
