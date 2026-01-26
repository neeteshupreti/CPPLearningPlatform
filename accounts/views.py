from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from learning.models import Chapter, UserAchievement, Achievement, UserProfile


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
        # profile_picture = request.FILES.get("profile_picture")  # new

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

        # Save profile picture if provided
        # The UserProfile is auto-created by the signal when user is saved
        # if profile_picture:
        #     profile = user.learning_profile
        #     profile.profile_picture = profile_picture
        #     profile.save()

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


# Logout
def logout_view(request):
    logout(request)
    return redirect('accounts:landing')


# Contact Form
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


# Dashboard (with profile info)
@login_required(login_url='accounts:login')
def dashboard_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    # Calculate level and XP
    level = (profile.xp // 100) + 1
    xp = profile.xp
    xp_next = level * 100  # XP required for next level

    # Progress in percent for progress bar
    progress_percent = int((xp / xp_next) * 100)

    # Top learners
    top_learners = UserProfile.objects.order_by('-xp')[:5]

    # Recent badges
    recent_badges = UserAchievement.objects.filter(user=request.user).order_by('-earned_at')[:5]

    # Chapters with unlock status
    from learning.models import UserChapterCompletion
    chapters_list = Chapter.objects.order_by("order")
    completed_chapters = UserChapterCompletion.objects.filter(user=request.user).values_list('chapter_id', flat=True)
    
    chapters = []
    for chapter in chapters_list:
        is_unlocked = chapter.order == 1 or (chapter.order - 1 <= max((c.order for c in chapters_list.filter(id__in=completed_chapters)), default=0))
        chapters.append({
            'id': chapter.id,
            'title': chapter.title,
            'image': chapter.image,
            'is_locked': not is_unlocked,
            'order': chapter.order
        })

    context = {
        'profile': profile,
        'level': level,
        'xp': xp,
        'xp_next': xp_next,
        'progress_percent': progress_percent,
        'top_learners': top_learners,
        'recent_badges': recent_badges,
        'chapters': chapters,
    }

    return render(request, 'accounts/dashboard.html', context)

