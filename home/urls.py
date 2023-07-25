from django.urls import path
from home.views import home, handle_login, registration

urlpatterns = [
    path("", home, name="home"),
    path("login", handle_login, name="login"),
    path("registration", registration, name="registration"),
]
