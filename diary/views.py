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

class DiaryCreateView(CreateView):
  template_name = 'diary/diary_create.html'
  form_class = DiaryForm
  success_url = reverse_lazy('diary:diary_create_complete')

class DiaryCreateCompleteView(TemplateView):
  template_name = 'diary/diary_create_complete.html'

class DiaryListView(ListView):
    template_name = 'diary/diary_list.html'
    model = Diary

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