from django.urls import path
from home.views import home, login, registration

urlpatterns = [
    path("", home, name="home"),
    path("login", login, name="login"),
    path("registration", registration, name="registration"),
]
