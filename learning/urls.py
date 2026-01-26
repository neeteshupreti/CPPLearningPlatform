from django.urls import path
from . import views

app_name = "learning"  # namespace for URLs

urlpatterns = [
    path('chapters/', views.chapter_list, name="chapter_list"),  # updated name
    path('chapter/<int:pk>/', views.chapter_detail, name="chapter_detail"),
    path('chapter/<int:chapter_id>/quiz/', views.chapter_quiz, name='chapter_quiz'),
    path('submit-quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
        path('chapters/<int:chapter_id>/complete/', views.complete_chapter, name='complete_chapter'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('achievements/', views.achievements, name='achievements'),
]
