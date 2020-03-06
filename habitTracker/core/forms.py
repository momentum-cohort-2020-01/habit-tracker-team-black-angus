from django import forms

from .models import Habit, Log

class LogForm(forms.Form):
    value_entry = forms.IntegerField()
