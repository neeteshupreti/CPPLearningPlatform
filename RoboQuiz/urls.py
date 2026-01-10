from django.contrib import admin

from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("chat/", include("chat.urls")),

]

from django.urls import path
from .views import game_home  # Import the view you just made

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_home, name='home'), # This maps the root URL to your game
]
