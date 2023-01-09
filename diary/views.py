from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import DiaryForm

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
