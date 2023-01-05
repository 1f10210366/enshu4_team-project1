from django.shortcuts import render

# Create your views here.
def weather(request):
  return render(request,'diary/weather.html')

def diary(request):
  return render(request, 'diary/diary.html')

def index(request):
  return render(request, 'diary/index.html')