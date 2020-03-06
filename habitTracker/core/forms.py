from django import forms

from .models import Habit, Log

class LogForm(forms.ModelForm):

    class Meta: 
        model = Log
        widgets = {'habit': forms.HiddenInput()}
        fields = ('value_entry','habit')
