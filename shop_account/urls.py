from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('account/sign-up/', views.signup, name='sign-up'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('log-out/', views.Logout.as_view(), name='log-out'),
]