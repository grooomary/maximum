from django.contrib import admin
from django.urls import path, include

from Django_projango.app_auth.views import profile, register, login_view, logout_view

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout')
]