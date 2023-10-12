from django import forms
from .models import Diary
from .models import Event

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text')
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            #'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        start_date = forms.IntegerField(required=True)
        end_date = forms.IntegerField(required=True)
        event_name = forms.CharField(required=True, max_length=32)

class CalendarForm(forms.Form):
   class Meta:
     model = Event
     start_date = forms.IntegerField(required=True)
     end_date = forms.IntegerField(required=True)