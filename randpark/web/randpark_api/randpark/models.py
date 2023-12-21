from django.db import models
from django.contrib import admin

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating_yellow = models.FloatField(default=72.0)
    rating_white = models.FloatField(default=72.0)
    rating_gold = models.FloatField(default=72.0)
    rating_red = models.FloatField(default=72.0)
    rating_blue = models.FloatField(default=72.0)
    record_mens = models.IntegerField(default="NULL")
    record_ladies = models.IntegerField(default="NULL")

    def __str__(self):
        return self.name

class TeeTimes(models.Model):
    time = models.TimeField("tee off time")

    def __str__(self):
        return str(self.time)
    
    @admin.display(
        boolean=True,
        ordering="time",
        description="Tee Off Time?",
    )
    
    def tee_off_time(self):
        return self.time

class Booking(models.Model):
    member_no_1 = models.CharField(max_length=6, default='', blank=True)
    member_no_2 = models.CharField(max_length=6, default='', blank=True)
    member_no_3 = models.CharField(max_length=6, default='', blank=True)
    member_no_4 = models.CharField(max_length=6, default='', blank=True)
    play_date = models.DateField("date to play")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    tee_time_id = models.ForeignKey(TeeTimes, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.play_date)
