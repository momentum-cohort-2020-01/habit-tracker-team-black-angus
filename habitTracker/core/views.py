from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from .models import Habit, Log
from .forms import LogForm, HabitForm


# Create your views here.
def launch_home(request):
    return render(request, 'core/home.html')

def habit_list(request):
    return render(request, 'core/habits.html')

def habit_detail(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    try:
        current_log = Log.objects.filter(habit_id=pk).latest('created_at').value_entry
    except Log.DoesNotExist:
        current_log = 0
    return render(request, 'core/habit_detail.html', {'habit':habit, 'pk': pk, 'current_log':current_log})

def log_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.habit = habit
            form.save()
            return redirect('habit-detail', pk=pk)
    else:
        form = LogForm()

    return render(request, 'core/log_habit.html', {'form':form})


# def habit_detail(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     log = Log.objects.filter(habit_id=pk).latest('created_at').value_entry
#     if request.method == "POST":
#         form = LogForm(request.POST, instance=log)

#         if form.is_valid():
#             log = form.save()
#             return redirect('habit-detail', pk=pk)
#     else:
#         form = LogForm()

#     return render(request, 'core/habit_detail.html', {'habit':habit, 'form':form, 'log':log, 'pk':pk })
    

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
        habit_pk = request.POST.get('habit')
        habit = Habit.objects.get(pk=habit_pk)
        value_entry = request.POST.get('value_entry')
        log = Log.objects.create(habit=habit, value_entry=value_entry)
        
    form = LogForm()
    return render(request, 'core/habits.html', {'habits': habits, 'form': form})

def post_log(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    form = LogForm()

def create_habit(request):
    usertemp = request.user
    if request.method == "POST":
        form = HabitForm(request.POST)
        name = request.POST.get('name')
        action = request.POST.get('action')
        goal = request.POST.get('goal')
        user = request.POST.get('user')
        if form.is_valid():
            form.save()
            return redirect('user-profile')
    else:    
        form = HabitForm()
    return render(request, 'core/createhabit.html', {'form': form})

