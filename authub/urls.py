from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegisterAPIView,
    DietitianRegisterAPIView,
    LoginView,
    LogoutView,
    PasswordResetConfirmView
)

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="user-register"),
    path("dietitian/register/", DietitianRegisterAPIView.as_view(), name="dietitian-register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
]