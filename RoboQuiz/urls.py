from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from .views import game_home  # Import the view you just made

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path("chat/", include("chat.urls")),
    path('learning/', include('learning.urls')),
    path('game/', include('game.urls')),
    # path('', game_home, name='home'), # This maps the root URL to your game
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)