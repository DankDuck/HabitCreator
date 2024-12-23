from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class BasicHabit(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dashboard')

class AdvancedHabit(models.Model):
    basic = models.OneToOneField(BasicHabit, on_delete=models.CASCADE, null=True, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    time = models.CharField(max_length=100, blank=True)
    place = models.CharField(max_length=100, blank=True)
    env_obvious = models.TextField(blank=True)
    habit_bundling = models.TextField(blank=True)
    culture = models.CharField(max_length=100, blank=True)
    figure = models.CharField(max_length=100, blank=True)
    benefits = models.TextField(blank=True)
    motivation_ritual = models.CharField(max_length=100, blank=True)
    habit_shaping = models.TextField(blank=True)
    reduce_friction = models.TextField(blank=True)
    incentive = models.TextField(blank=True)
    progress = models.TextField(blank=True)
    
    def __str__(self):
        return self.basic.name
    
    def get_absolute_url(self):
        return reverse('dashboard')
    