from django.urls import path
from dashboard.views import dashboard, my_links, short_url

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("links", my_links, name="my_links"),
    path("short-url", short_url, name="short_url"),
]
