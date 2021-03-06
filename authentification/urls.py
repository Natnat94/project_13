from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, 
)

from .views import (
    register,
    profil,
    change_password,
    login,
    logout,
    confirmation_email,
)


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("password/", change_password, name="change_password"),
    path("logout/", logout, name="logout"),
    path("profil/", profil, name="profil"),
    path("confirm/", confirmation_email),
    path("confirm/<str:token>/", confirmation_email),
    # Token generated by the 'login' view
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
