from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Habit, Log


# Create your views here.
def launch_home(request):
    return render(request, 'core/home.html')

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habit})