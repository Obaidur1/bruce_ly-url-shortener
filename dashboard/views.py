from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Short_URL


# Create your views here.
@login_required(login_url="login")
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def my_links(request):
    user_links = Short_URL.objects.filter(owner=request.user)
    link_count = len(user_links)
    return render(
        request,
        "dashboard/my_links.html",
        {"user_links": user_links, "link_count": link_count},
    )


def short_url(request):
    if request.method == "GET":
        return render(request, "dashboard/short_url.html")
    elif request.method == "POST":
        if "link_submit" in request.POST:
            long_url = request.POST["long_url"]
            long_url = long_url.strip()
            short_url = request.POST["short_url"]
            shortend_url = Short_URL(
                short_url=short_url, long_url=long_url, owner=request.user
            )
            shortend_url.save()
            return redirect("my_links")
