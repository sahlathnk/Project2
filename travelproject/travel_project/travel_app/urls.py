from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('addition/',views.add,name='add')
]
