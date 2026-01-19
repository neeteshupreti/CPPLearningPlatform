from django.urls import path
from . import views

app_name = "learning"  # namespace for URLs

urlpatterns = [
    path('chapters/', views.chapter_list, name="chapter"),  # fixed name
    path('chapter/<int:pk>/', views.chapter_detail, name="chapter_detail"),
    path('chapter/<int:chapter_id>/quiz/', views.chapter_quiz, name='chapter_quiz'),
    path('submit-quiz/<int:quiz_id>/', views.submit_quiz, name='submit_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),  # removed duplicate
    path('achievements/', views.achievements, name='achievements'),
]
