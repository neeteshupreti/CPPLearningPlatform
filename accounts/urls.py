from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.landing_view, name="landing"),   # landing page
    path("signup/", views.register_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path('contact/', views.contact_view, name='contact'),

]
