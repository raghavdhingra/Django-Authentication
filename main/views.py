from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    return render(request, "login.html")


def loginRequest(request):
    if request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        page = request.POST.get("page")
        role = request.POST.get("role")
        print(user, password, page, role)
        context = "ADMIN"
        return HttpResponse(context)
    return HttpResponse("You're not allowed to access this page")


def signup(request):
    return render(request, "signup.html")
