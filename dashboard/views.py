from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def my_links(request):
    return render(request, "dashboard/my_links.html")


def short_url(request):
    return render(request, "dashboard/short_url.html")
