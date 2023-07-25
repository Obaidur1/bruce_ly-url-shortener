from django.urls import path
from home.views import (
    home,
    handle_login,
    handle_logout,
    registration,
    redirect_to_original,
)

urlpatterns = [
    path("", home, name="home"),
    path("login", handle_login, name="login"),
    path("logout", handle_logout, name="logout"),
    path("registration", registration, name="registration"),
    path("<str:short_url>", redirect_to_original),
]
