from dj_rest_auth.registration.views import (
    ConfirmEmailView,
    RegisterView,
    VerifyEmailView,
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
    path("password-reset/", PasswordResetView.as_view()),
    path(
        "password-reset-confirm/<int:uidb64>/str:token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
