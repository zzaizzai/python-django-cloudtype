from . import views
from django.urls import path, include

urlpatterns = [
    path('login_user', views.login_user, name="login_user"),
    path('register_user', views.register_user, name="register_user"),
    path('logout_user', views.logout_user, name="logout_user"),
]
