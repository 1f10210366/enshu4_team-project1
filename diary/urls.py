from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("diary/", views.diary, name="diary"),
    path("whather/", views.weather, name="weather"),
    path("schedule/", views.schedule, name="schedule"), 
]