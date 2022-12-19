from . import views
from django.urls import path, include

urlpatterns = [
    path('login', views.login_user, name="login_user"),
    path('logout', views.logout_user, name="logout"),
]
