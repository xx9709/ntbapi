from django.urls import path
from .views import RegiserView, UserView, LogoutView, LoginView, RefreshTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
     path('register', RegiserView.as_view()),
     path('login', LoginView.as_view(), name='token_obtain_pair'),
     path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
     path('user', UserView.as_view()),
     path('logout', LogoutView.as_view()),
     path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
