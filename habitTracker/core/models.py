from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    goal = models.CharField(max_length=15)

class Log(models.Model):
    user = models.ForeignKey(to=User, related_name='logs', on_delete=models.CASCADE)
    habit = models.ForeignKey(to=Habit, related_name='habits', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value_entry = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} '



