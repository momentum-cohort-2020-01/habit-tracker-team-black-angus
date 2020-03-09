from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    goal = models.CharField(max_length=15)
    user = models.ForeignKey(to=User, related_name='logs', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'
    
    @property
    def current_log(self):
        try:
            current_log = Log.objects.filter(habit_id=self.pk).latest('created_at').value_entry
        except Log.DoesNotExist:
            current_log = 0
        return current_log
    
    @property
    def goal_met(self):
        goal_met = self.current_log >= int(self.goal)
        return goal_met

        
class Log(models.Model):
    habit = models.ForeignKey(to=Habit, related_name='habits', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value_entry = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.habit}: {self.value_entry}'
