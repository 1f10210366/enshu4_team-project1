from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("diary/", views.diary, name="diary"),
    path("whather/", views.weather, name="weather"),
    path("schedule/", views.schedule, name="schedule"), 
    path("diary/create/", views.DiaryCreateView.as_view(), name='diary_create'),
    path("diary/create/complete/", views.DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
]