from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path("", views.TopView.as_view(), name="top"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    #path("", views.IndexView.as_view(), name="index"),
    path("diary/", views.diary, name="diary"),
    path("whather/", views.weather, name="weather"),
    path("schedule/", views.schedule, name="schedule"),
    path("schedule/add/", views.add_event, name="add_event"),
    path("schecule/lst/", views.get_events, name="get_events"), 
    path("diary/create/", views.DiaryCreateView.as_view(), name='diary_create'),
    path("diary/create/complete/", views.DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
    path('diary/list/', views.DiaryListView.as_view(), name='diary_list'),
    path('diary/detail/<uuid:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/update/<uuid:pk>/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/delete/<uuid:pk>/', views.DiaryDeleteView.as_view(), name='diary_delete'),

]