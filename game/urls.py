from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.game_view, name='game'),
    path('update_xp/', views.update_xp, name='update_xp'),
]