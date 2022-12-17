from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.join, name='join'),
    path('mypage', views.mypage, name='mypage'),
    path('login', views.login, name='login'),
]
