from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm

# Landing page (HOME)
def landing_view(request):
    return render(request, "accounts/landing.html")

def home(request):
    return render(request, "accounts/landing.html")

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
        if user:
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

# Contact form view
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('accounts:contact')
    else:
        form = ContactForm()
    return render(request, "accounts/contact.html", {"form": form})
