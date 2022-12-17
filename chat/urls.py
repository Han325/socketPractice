from atexit import register
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.random, name="home_page"),
]