from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary
from django.utils import timezone



# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


from . import forms

#signup
from django.contrib.auth import login
from django.urls import reverse_lazy

from .forms import SignUpForm

#スケジュール
import json
from .models import Event
from .forms import EventForm
from django.http import Http404
from django.http import JsonResponse
import time
from django.template import loader
from django.http import HttpResponse
from django.middleware.csrf import get_token




class TopView(TemplateView):
    template_name = "diary/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "diary/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "diary/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "diary/logout.html"

class IndexView(TemplateView):
  template_name = 'diary/index.html'

def weather(request):
  return render(request,'diary/weather.html')

def diary(request):
  return render(request, 'diary/diary.html')

def schedule(request):
  return render(request, 'diary/schedule.html')

#日記帳

class DiaryCreateView(CreateView):
  template_name = 'diary/diary_create.html'
  form_class = DiaryForm
  success_url = reverse_lazy('diary:diary')
  def form_valid(self, form):
        form.instance.contributer = self.request.user.get_username()
        return super().form_valid(form)

class DiaryCreateCompleteView(TemplateView):
  template_name = 'diary/diary_create_complete.html'

class DiaryListView(LoginRequiredMixin,ListView):
    template_name = 'diary/diary_list.html'
    model = Diary
    # クエリセットのカスタマイズが必要な場合
    def get_queryset(self):
        # ログインユーザーの日記のみをフィルタリング
        return Diary.objects.filter(contributer=self.request.user.get_username()).order_by('-created_at')
   

class DiaryDetailView(DetailView):
    template_name = 'diary/diary_detail.html'
    model = Diary

class DiaryUpdateView(UpdateView):
    template_name = 'diary/diary_update.html'
    model = Diary
    fields = ('date', 'title', 'text',)
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.updated_at = timezone.now()
        diary.save()
        return super().form_valid(form)

class DiaryDeleteView(DeleteView):
    template_name = 'diary/diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
    #Call the delete() method on the fetched object and then redirect to thesuccess URL.
      self.object = self.get_object()
      success_url = self.get_success_url()
      self.object.delete()
      return HttpResponseRedirect(success_url)
    
#ログイン
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "diary/signup.html"
    success_url = reverse_lazy("diary:top")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
    

 #スケジュール表
def index(request):
    """
    カレンダー画面
    """
    # CSRFのトークンを発行する
    get_token(request)

    template = loader.get_template("scheduleCalendar/index.html")
    return HttpResponse(template.render())


def add_event(request):
    """
    イベント登録
    """

    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # バリデーション
    eventForm = EventForm(datas)
    if eventForm.is_valid() == False:
        # バリデーションエラー
        raise Http404()

    # リクエストの取得
    start_date = datas["start_date"]
    end_date = datas["end_date"]
    event_name = datas["event_name"]

    # 日付に変換。JavaScriptのタイムスタンプはミリ秒なので秒に変換
    formatted_start_date = time.strftime(
        "%Y-%m-%d", time.localtime(start_date / 1000))
    formatted_end_date = time.strftime(
        "%Y-%m-%d", time.localtime(end_date / 1000))

    # 登録処理
    event = Event(
        event_name=str(event_name),
        start_date=formatted_start_date,
        end_date=formatted_end_date,
    )
    event.save()

    # 空を返却
    return HttpResponse("")


def get_events(request):
    """
    イベントの取得
    """

    if request.method == "GET":
        # GETは対応しない
        raise Http404()

    # JSONの解析
    datas = json.loads(request.body)

    # バリデーション
    calendarForm = CalendarForm(datas)
    if calendarForm.is_valid() == False:
        # バリデーションエラー
        raise Http404()

    # リクエストの取得
    start_date = datas["start_date"]
    end_date = datas["end_date"]

    # 日付に変換。JavaScriptのタイムスタンプはミリ秒なので秒に変換
    formatted_start_date = time.strftime(
        "%Y-%m-%d", time.localtime(start_date / 1000))
    formatted_end_date = time.strftime(
        "%Y-%m-%d", time.localtime(end_date / 1000))

    # FullCalendarの表示範囲のみ表示
    events = Event.objects.filter(
        start_date__lt=formatted_end_date, end_date__gt=formatted_start_date
    )

    # fullcalendarのため配列で返却
    list = []
    for event in events:
        list.append(
            {
                "title": event.event_name,
                "start": event.start_date,
                "end": event.end_date,
            }
        )

    return JsonResponse(list, safe=False)