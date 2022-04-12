
from django.contrib import admin
from django.urls import path
from .views import home, profile

urlpatterns = [path('', home, name = "home"), path('add-profile/', profile, name = 'profile')]
