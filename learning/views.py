from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import (
    Chapter,
    Quiz,
    Question,
    UserAnswer,
    UserProfile,
    Achievement,
    UserAchievement
)

# =========================
# CHAPTER LIST
# =========================
def chapter_list(request):
    chapters = Chapter.objects.order_by("order")
    return render(request, "learning/chapter.html", {
        "chapters": chapters
    })


# =========================
# CHAPTER DETAIL
# =========================
def chapter_detail(request, pk):
    chapter = get_object_or_404(Chapter, pk=pk)
    return render(request, "learning/chapter_detail.html", {
        "chapter": chapter
    })


# =========================
# CHAPTER QUIZ
# =========================
@login_required
def chapter_quiz(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)

    quiz = chapter.quizzes.first()
    if not quiz:
        return HttpResponse("No quiz available for this chapter.", status=404)

    questions = quiz.questions.all()

    return render(request, "learning/chapter_quiz.html", {
        "chapter": chapter,
        "quiz": quiz,
        "questions": questions
    })


# =========================
# SUBMIT QUIZ + XP + LEVEL + ACHIEVEMENTS
# =========================
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

    # =========================
    # XP & LEVEL LOGIC
    # =========================
    xp_earned = correct_count * 10  # 10 XP per correct answer

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    profile.xp += xp_earned
    profile.level = (profile.xp // 100) + 1
    profile.save()

    # =========================
    # ACHIEVEMENT CHECK
    # =========================
    achievements = Achievement.objects.filter(
        xp_required__lte=profile.xp
    )

    for achievement in achievements:
        UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement
        )

    # =========================
    # SCORE
    # =========================
    score_percent = int((correct_count / total_questions) * 100) if total_questions > 0 else 0

    return render(request, "learning/quiz_result.html", {
        "quiz": quiz,
        "total": total_questions,
        "correct": correct_count,
        "score": score_percent,
        "xp": xp_earned,
        "level": profile.level
    })


# =========================
# LEADERBOARD
# =========================
def leaderboard(request):
    profiles = UserProfile.objects.order_by('-xp')
    return render(request, "learning/leaderboard.html", {
        "profiles": profiles
    })


# =========================
# USER ACHIEVEMENTS
# =========================
@login_required
def achievements(request):
    achievements = UserAchievement.objects.filter(user=request.user)
    return render(request, "learning/achievements.html", {
        "achievements": achievements
    })
