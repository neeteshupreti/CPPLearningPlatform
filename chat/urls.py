<<<<<<< HEAD
from django.urls import path
from .views import chat_view
app_name = "chat"

urlpatterns = [
    path("", chat_view, name="chat"),
]
=======
from django.urls import path
from .views import chat_view

urlpatterns = [
    path("", chat_view, name="chat"),
]
>>>>>>> 3d5c8dafa1c7522f9648891421193305a5191b1e
