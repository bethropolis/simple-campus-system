from django import forms
from .models import School, Student, Faculty, Course

class SchoolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = School
        fields = ['name', 'location', 'description', 'established_date']
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))
        
class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration_in_months', 'school']
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label
    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'school', 'course']
        

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'date_added']
