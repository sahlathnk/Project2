from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register',views.registerfn,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]