from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import Habit, Log
from .forms import LogForm


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
    habits = Habit.objects.filter(user=request.user)
    if request.method == "POST":
        form = LogForm(request.POST)
        new_log = form.save(commit=False)
    form = LogForm()
    breakpoint()
    return render(request, 'core/habits.html', {'habits': habits, 'form': form})

def post_log(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    form = LogForm()

