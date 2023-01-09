from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import DiaryForm
from .models import Diary

# Create your views here.

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