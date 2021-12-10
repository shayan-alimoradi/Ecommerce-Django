from django.urls import path
from . import views

app_name = "account"


urlpatterns = [
    path("account/sign-in/", views.SignIn.as_view(), name="sign_in"),
    path("account/sign-up/", views.SignUp.as_view(), name="sign_up"),
    path("activate/<uidb64>/<token>/", views.ActiveEmail.as_view(), name="activate"),
    path("log-out/", views.Logout.as_view(), name="log_out"),
    path("profile/", views.UserProfile.as_view(), name="profile"),
    path("change-password/", views.ChangePassword.as_view(), name="change_pass"),
    path("user-panel/", views.UserPanel.as_view(), name="user_panel"),
    path("password-reset/", views.ResetPassword.as_view(), name="reset"),
    path("password-done/", views.DonePassword.as_view(), name="done"),
    path(
        "confirm-password/<uidb64>/<token>/",
        views.ConfirmPassword.as_view(),
        name="confirm",
    ),
    path(
        "complete-reset-password/", views.CompeletePassword.as_view(), name="complete"
    ),
    path("purchase-history/", views.history, name="history"),
]
