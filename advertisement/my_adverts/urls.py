from django.shortcuts import render
from django.urls import path
from .views import *

urlpatterns = [
    path('index.html', index, name='index'),
    path('top-sellers.html', topSellers, name='top-sellers'),
    path('advertisement-post.html', advertisementPost, name='advertisement-post'),
    path('register.html', register, name='register'),
    path('login.html', login, name='login'),
    path('profile.html', profile, name='profile'),
    path('advertisement.html', profile, name='advertisement'),
]