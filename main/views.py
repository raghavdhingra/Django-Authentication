from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Login
# Create your views here.


def home(request):
    return render(request, "login.html")


def loginRequest(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        page = request.POST.get("page")
        role = request.POST.get("role")
        context = role
        if page == "login":
            req_user = Login.objects.filter(
                username=user, password=password, role=role)
            if len(req_user) > 0:
                return HttpResponse(context)
            else:
                return HttpResponse("Incorrect Username or password")
        else:
            req_user = Login.objects.create(
                username=user, password=password, role=role)
            req_user.save()
            return HttpResponse(context)
    return HttpResponse("You're not allowed to access this page")


def signup(request):
    return render(request, "signup.html")
