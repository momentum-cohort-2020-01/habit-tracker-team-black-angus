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

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method == "POST":
        form = LogForm(request.POST)
        # habit_pk = request.POST.get('habit')
        # habit = Habit.objects.get(pk=habit_pk)
        if form.is_valid():
            form.save()
        return redirect('habit-list')
    else:
        form = LogForm()
    
    #     value_entry = request.POST.get('value_entry')
    #     log = Log.objects.create(habit=habit, value_entry=value_entry)
        
    # form = LogForm()
    # return render(request, 'core/habit_detail.html', {'habit':habit, "pk":pk})
    return render(request, 'core/habit_detail.html', {'habit':habit, 'form':form })

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

