from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "index.html")


def handle_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        if "login_submit" in request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                temp_user = User.objects.get(email=email)
                user = authenticate(
                    request, username=temp_user.username, password=password
                )
                if user is not None:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    return HttpResponse("Username or password not matched")
            except User.DoesNotExist:
                return HttpResponse("Does not exist")


def registration(request):
    if request.method == "GET":
        return render(request, "registration.html")
    elif request.method == "POST":
        if "registration_submit" in request.POST:
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            if password1 != password2:
                return HttpResponse("Password not matched")
            user = User.objects.create_user(
                username=username, email=email, password=password2
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return redirect("login")
