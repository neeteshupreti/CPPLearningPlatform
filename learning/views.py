from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Chapter, Quiz, Question, UserAnswer, UserProfile, Achievement, UserAchievement, Badge, UserChapterCompletion
from .utils import award_badge

# ----------------------------
# CHAPTER LIST
# ----------------------------
@login_required
def chapter_list(request):
    chapters = Chapter.objects.order_by("order")
    
    # Get chapters completed by the current user
    completed_chapters = UserChapterCompletion.objects.filter(user=request.user).values_list('chapter_id', flat=True)
    
    # Build chapter status: unlock chapters based on previous chapter completion
    chapter_data = []
    for chapter in chapters:
        # First chapter is always unlocked
        is_unlocked = chapter.order == 1 or (chapter.order - 1 <= max(c.order for c in Chapter.objects.filter(id__in=completed_chapters)) if completed_chapters else False)
        is_completed = chapter.id in completed_chapters
        
        chapter_data.append({
            'chapter': chapter,
            'is_unlocked': is_unlocked,
            'is_completed': is_completed
        })
    
    return render(request, "learning/chapter.html", {"chapters": chapter_data})

# ----------------------------
# CHAPTER DETAIL
# ----------------------------
@login_required
def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    
    # Check if chapter is unlocked for this user
    completed_chapters = UserChapterCompletion.objects.filter(user=request.user).values_list('chapter__order', flat=True)
    
    # User can access if chapter is first or previous chapter is completed
    can_access = chapter.order == 1 or (chapter.order - 1) in completed_chapters
    
    if not can_access:
        return HttpResponse("This chapter is locked. Complete the previous chapter first.", status=403)
    
    return render(request, "learning/chapter_detail.html", {"chapter": chapter})

# ----------------------------
# CHAPTER QUIZ
# ----------------------------
@login_required
def chapter_quiz(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    
    # Check if chapter is unlocked for this user
    completed_chapters = UserChapterCompletion.objects.filter(user=request.user).values_list('chapter__order', flat=True)
    
    # User can access if chapter is first or previous chapter is completed
    can_access = chapter.order == 1 or (chapter.order - 1) in completed_chapters
    
    if not can_access:
        return HttpResponse("This chapter is locked. Complete the previous chapter first.", status=403)
    
    quiz = chapter.quizzes.first()
    if not quiz:
        return HttpResponse("No quiz available for this chapter.", status=404)
    questions = quiz.questions.all()
    return render(request, "learning/chapter_quiz.html", {
        "chapter": chapter,
        "quiz": quiz,
        "questions": questions
    })

# ----------------------------
# SUBMIT QUIZ + XP + LEVEL + ACHIEVEMENTS
# ----------------------------
@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    total_questions = quiz.questions.count()
    correct_count = 0

    if request.method == "POST":
        for question in quiz.questions.all():
            selected_option = request.POST.get(f"question_{question.id}")
            if not selected_option:
                continue
            selected_option = int(selected_option)
            is_correct = selected_option == question.correct_option
            if is_correct:
                correct_count += 1
            UserAnswer.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )

    # XP & LEVEL LOGIC
    xp_earned = correct_count * 10  # 10 XP per correct answer
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    profile.xp += xp_earned
    profile.level = (profile.xp // 100) + 1
    profile.save()

    score_percent = int((correct_count / total_questions) * 100) if total_questions > 0 else 0

    # ACHIEVEMENT / BADGES
    # 1️⃣ Chapter completion badge
    if correct_count == total_questions and total_questions > 0:
        chapter = quiz.chapter
        # Award chapter completion badge
        award_badge(request.user, "Chapter King")
        
        # Mark chapter as completed to unlock next chapters
        UserChapterCompletion.objects.get_or_create(user=request.user, chapter=chapter)

    # 2️⃣ Perfect quiz badge
    if score_percent == 100:
        award_badge(request.user, "Quiz Master")

    # 3️⃣ XP milestone badges
    if profile.xp >= 100:
        award_badge(request.user, "Top Leveler")
    if profile.xp >= 500:
        award_badge(request.user, "Supreme Warrior")

    return render(request, "learning/quiz_result.html", {
        "quiz": quiz,
        "total": total_questions,
        "correct": correct_count,
        "score": score_percent,
        "xp": xp_earned,
        "level": profile.level
    })

# ----------------------------
# LEADERBOARD
# ----------------------------
def leaderboard(request):
    profiles = UserProfile.objects.order_by('-xp').select_related('user')
    
    # Build leaderboard data with rankings and stats
    leaderboard_data = []
    current_user_rank = None
    
    for index, profile in enumerate(profiles, 1):
        # Count completed chapters for this user
        completed_chapters = UserChapterCompletion.objects.filter(user=profile.user).count()
        
        # Count total quiz answers for this user
        total_answers = UserAnswer.objects.filter(user=profile.user).count()
        
        item = {
            'rank': index,
            'user': profile.user,
            'profile': profile,
            'username': profile.user.username,
            'xp': profile.xp,
            'level': profile.level,
            'completed_chapters': completed_chapters,
            'total_answers': total_answers,
            'is_current_user': request.user.is_authenticated and profile.user == request.user,
        }
        leaderboard_data.append(item)
        
        if request.user.is_authenticated and profile.user == request.user:
            current_user_rank = index
    
    # Calculate global stats
    total_users = UserProfile.objects.count()
    total_xp = sum(p.xp for p in profiles)
    total_completions = UserChapterCompletion.objects.count()
    avg_level = sum(p.level for p in profiles) / total_users if total_users > 0 else 0
    
    context = {
        'leaderboard': leaderboard_data,
        'current_user_rank': current_user_rank,
        'total_users': total_users,
        'total_xp': total_xp,
        'total_completions': total_completions,
        'avg_level': round(avg_level, 1),
    }
    return render(request, "learning/leaderboard.html", context)

# ----------------------------
# USER ACHIEVEMENTS
# ----------------------------
@login_required
def achievements(request):
    user_profile = request.user.learning_profile
    
    # Get all badges
    all_badges = Badge.objects.all()
    total_badges = all_badges.count()
    
    # Prepare badge data for template
    badges = []
    unlocked_count = 0
    
    for badge in all_badges:
        # Check if user has this badge
        is_unlocked = UserAchievement.objects.filter(user=request.user, badge=badge).exists()
        if is_unlocked:
            unlocked_count += 1
            earned_at = UserAchievement.objects.filter(user=request.user, badge=badge).first().earned_at
            date_earned = earned_at.date()
        else:
            date_earned = None
        
        # Hardcode some attributes for now
        badge_data = {
            'name': badge.name,
            'is_unlocked': is_unlocked,
            'icon_emoji': '🏆',  # Default emoji
            'required_chapter': None,  # Will set based on name or logic
            'date_earned': date_earned,
        }
        
        # Customize based on badge name
        if 'Supreme' in badge.name:
            badge_data['icon_emoji'] = '👑'
            badge_data['required_chapter'] = 'All Chapters'
        elif 'Quiz' in badge.name:
            badge_data['icon_emoji'] = '🧠'
            badge_data['required_chapter'] = 'Perfect Quiz'
        elif 'Chapter' in badge.name:
            badge_data['icon_emoji'] = '📖'
            badge_data['required_chapter'] = 'Complete Chapter'
        elif 'Level' in badge.name:
            badge_data['icon_emoji'] = '⭐'
            badge_data['required_chapter'] = 'Reach Level'
        
        badges.append(badge_data)
    
    context = {
        'user_profile': user_profile,
        'badges': badges,
        'unlocked_count': unlocked_count,
        'total_badges': total_badges,
        'xp_percent': user_profile.xp % 100,
    }
    
    return render(request, "learning/achievements.html", context)

# ----------------------------
# COMPLETE CHAPTER & AWARD XP/BADGES
# ----------------------------
@login_required
def complete_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    profile = UserProfile.objects.get(user=request.user)

    # Add XP for completing chapter
    profile.xp += 50
    profile.level = (profile.xp // 100) + 1
    profile.save()

    # Award badges based on milestones
    if profile.xp >= 100:
        award_badge(request.user, "100 XP Badge")
    if profile.level >= 2:
        award_badge(request.user, "Level 2 Badge")
    if chapter.order == 1:  # first chapter
        award_badge(request.user, "First Chapter Completed")

    return redirect('accounts:dashboard')

def achievements_view(request):
    # Get logged-in user's profile
    profile = request.user.learning_profile

    # Get user's earned achievements
    achievements = UserAchievement.objects.filter(user=request.user).select_related('achievement', 'badge').order_by('-earned_at')

    # Total badges in system
    total_badges = Badge.objects.count()

    # Progress for XP bar
    xp = profile.xp
    level = profile.level
    xp_next = level * 100
    progress_percent = int((xp / xp_next) * 100) if xp_next else 0

    context = {
        'profile': profile,
        'achievements': achievements,
        'total_badges': total_badges,
        'progress_percent': progress_percent,
        'xp_next': xp_next,
    }
#     return render(request, 'achievements.html', context)
# @login_required
# def chapter_list(request):
#     chapters = Chapter.objects.order_by('order')
    
#     # Chapters completed by the user
#     completed_chapters = UserChapterCompletion.objects.filter(user=request.user, completed=True).values_list('chapter_id', flat=True)

#     # For template: determine locked/unlocked
#     chapter_status = []
#     for chapter in chapters:
#         if chapter.order == 1 or (chapter.order - 1 in completed_chapters):
#             locked = False
#         else:
#             locked = True
#         chapter_status.append({
#             'chapter': chapter,
#             'locked': locked,
#             'completed': chapter.id in completed_chapters
#         })

#     context = {
#         'chapter_status': chapter_status
#     }
#     return render(request, 'learning/chapter_list.html', context)

# @login_required
# def complete_chapter(request, chapter_id):
#     chapter = get_object_or_404(Chapter, id=chapter_id)
#     # Mark as completed
#     completion, created = UserChapterCompletion.objects.get_or_create(user=request.user, chapter=chapter)
#     completion.completed = True
#     completion.save()

#     # Award a badge automatically
#     profile = request.user.learning_profile
#     badge, _ = Badge.objects.get_or_create(name=f"{chapter.title} Completed")
#     profile.badges.add(badge)
#     profile.save()

#     return redirect('learning:chapter_list')