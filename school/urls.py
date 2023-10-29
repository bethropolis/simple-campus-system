from django.urls import path
from . import views

urlpatterns = [
    path('schools/new/', views.add_school, name='add_school'),
    path('schools/', views.list_schools, name='list_schools'),
    path('student/new/', views.add_student, name='add_student'),
    path('students/', views.list_students, name='list_students'),
]
