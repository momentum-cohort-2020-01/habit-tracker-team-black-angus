from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import Habit, Log


# Create your views here.
def launch_home(request):
    return render(request, 'core/home.html')

def habit_list(request):
    return render(request, 'core/habits.html')

def register_user(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habits-list')
    else:
        form = UserCreationForm()
    return(request, 'core/register.html', {'form': form})

def user_profile(request):
    habits = Habit.objects.all()
    logs = Log.objects.all()
    print(habits)
    print(logs)
    return render(request, 'core/habits.html', {'habits': habits})

