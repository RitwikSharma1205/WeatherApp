from unicodedata import name
from django.contrib import admin
from django.urls import path

from weather.views import home
urlpatterns = [
    path('',home,name="home")
]