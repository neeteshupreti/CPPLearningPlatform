from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path('', views.game_home, name='home'),
    path('quiz/<int:question_id>/', views.quiz_view, name='quiz'),
    path('check/<int:question_id>/', views.check_answer, name='check'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
