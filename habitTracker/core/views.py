from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def launch_home(request):
    return render(request, 'core/home.html')

def habit_list(request):
    return render(request, 'core/habits.html')