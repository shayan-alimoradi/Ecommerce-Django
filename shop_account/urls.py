from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('account/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('account/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('activate/<uidb64>/<token>/', views.ActiveEmail.as_view(), name='activate'),
    path('log-out/', views.Logout.as_view(), name='log-out'),
]