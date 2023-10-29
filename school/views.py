from django.shortcuts import render, redirect
from .models import School, Student
from .forms import SchoolForm, StudentForm

def add_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_schools')  # Redirect to the list of schools
    else:
        form = SchoolForm()
    return render(request, 'add_school.html', {'form': form})

def list_schools(request):
    schools = School.objects.all()
    return render(request, 'list_schools.html', {'schools': schools})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})