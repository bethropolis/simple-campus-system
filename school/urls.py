from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name='index'),
    path('schools/new/', views.add_school, name='add_school'),
    path('school/<int:school_id>/edit/', views.edit_school, name='edit_school'),
    path('school/<int:school_id>/delete/', views.delete_school, name='delete_school'),
    path('schools/', views.list_schools, name='list_schools'),
    path('student/new/', views.add_student, name='add_student'),
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    path('students/', views.list_students, name='list_students'),
    path('course/new/', views.add_course, name='add_course'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete', views.delete_course, name='delete_course'),
    path('courses/', views.list_courses, name='list_courses'),
    path('faculty/new/', views.add_faculty, name='add_faculty'),
    path('faculty/', views.list_faculty, name='list_faculty'),
]
