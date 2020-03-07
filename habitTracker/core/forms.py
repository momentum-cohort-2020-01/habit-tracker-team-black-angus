from django import forms

from .models import Habit, Log



class LogForm(forms.ModelForm):

    class Meta: 
        model = Log
        fields = ('value_entry', )


class HabitForm(forms.ModelForm):

    class Meta: 
        model = Habit
        fields = ('name', 'action', 'goal', 'user')







# class LogForm(forms.Form):
#     value_entry = forms.IntegerField()
