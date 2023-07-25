from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def my_links(request):
    return render(request, "dashboard/my_links.html")


def short_url(request):
    return render(request, "dashboard/short_url.html")
