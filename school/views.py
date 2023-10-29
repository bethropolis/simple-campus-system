from django.shortcuts import render, redirect, get_object_or_404
from .models import School, Student, Course, Faculty
from .forms import SchoolForm, StudentForm, CourseForm, FacultyForm


def index_page(request):
    return render(request, 'index.html')

def add_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_schools')
    else:
        form = SchoolForm()
    return render(request, 'add_school.html', {'form': form})

def list_schools(request):
    schools = School.objects.all()
    return render(request, 'list_schools.html', {'schools': schools})

def edit_school(request, school_id):
    school = get_object_or_404(School, pk=school_id)

    if request.method == "POST":
        form = SchoolForm(request.POST, instance=school)
        if form.is_valid():
            form.save()
            return redirect('list_schools')
    else:
        form = SchoolForm(instance=school)
    return render(request, 'edit_school.html', {'form': form, 'school': school})

def delete_school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    if request.method == "POST":
        school.delete()
        return redirect('list_schools')
    return render(request, 'delete_school.html', {'school': school})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('list_students')
    return render(request, 'delete_student.html', {'student': student})

def list_students(request):
    students = Student.objects.all()
    return render(request, 'list_students.html', {'students': students})

def add_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'edit_course.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        course.delete()
        return redirect('list_courses')
    return render(request, 'delete_course.html', {'course': course})

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'list_courses.html', {'courses': courses})


def add_faculty(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_faculty')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})

def list_faculty(request):
    faculty = Faculty.objects.all()
    return render(request, 'list_faculty.html', {'faculty': faculty})
