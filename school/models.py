from django.db import models
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="main", null=True, blank=True)
    description = models.TextField(default='')
    established_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    duration_in_months = models.PositiveIntegerField(default=48)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=10, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_admission = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

