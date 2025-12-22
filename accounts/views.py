from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "accounts/landing.html")  # rename according to your landing page template

# Signup / Register
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('accounts:signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return redirect('accounts:signup')

        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('accounts:login')

    return render(request, "accounts/register.html")

# Login
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('accounts:login')
    return render(request, "accounts/login.html")

# Dashboard (requires login)
@login_required(login_url='accounts:login')
def dashboard_view(request):
    return render(request, "accounts/dashboard.html", {"user": request.user})

# Logout
def logout_view(request):
    logout(request)
    return redirect('accounts:landing')
