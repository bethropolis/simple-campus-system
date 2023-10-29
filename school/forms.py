from django import forms
from .models import School, Student, Faculty, Course

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name']
        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'school'] 
        template_name = 'student_form.html' # specify the template to use
        success_url = '/students/' 

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'school']