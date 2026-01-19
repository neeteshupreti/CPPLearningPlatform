from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from learning.models import Chapter, UserAchievement, Achievement, UserProfile  # Import from learning app
from django.contrib.auth.models import User


# Landing page (HOME)
def landing_view(request):
    return render(request, "accounts/landing.html")


# Signup / Register
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profile_picture = request.FILES.get("profile_picture")  # new

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

        # Save profile picture
        if profile_picture:
            user.userprofile.profile_picture = profile_picture
            user.userprofile.save()

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
    return render(request, "accounts/dashboard.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect('accounts:landing')

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
# views.py
def dashboard_view(request):
    chapters = Chapter.objects.order_by('order')
    top_learners = UserProfile.objects.order_by('-xp')[:5]
    recent_badges = UserAchievement.objects.filter(user=request.user).order_by('-earned_at')[:5]

    # For progress
    xp = request.user.userprofile.xp if hasattr(request.user, 'userprofile') else 0
    level = (xp // 100) + 1
    xp_next = ((level) * 100)

    progress_percent = min(100, int((xp % 100) / 100 * 100))

    context = {
        'user': request.user,
        'chapters': chapters,
        'top_learners': top_learners,
        'recent_badges': recent_badges,
        'xp': xp,
        'level': level,
        'xp_next': xp_next,
        'progress_percent': progress_percent,
    }
    return render(request, 'accounts/dashboard.html', context)
