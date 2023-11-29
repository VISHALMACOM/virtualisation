from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# URL Configuration object
urlpatterns = [
    path('hello/', views.say_hello),
    path('teachers/', views.display_teachers, name='display_teachers'),
    path('courses/', views.display_courses, name='display_courses'),
    path('classes/', views.display_classes, name='display_classes'),
    path('students/', views.display_students, name='display_students'),
    path('attendance/', views.display_attendance, name='display_attendance'),
    path('timetable/', views.display_timetable, name='display_timetable'),
    path('rooms/', views.display_rooms, name='display_rooms'),
    path('timetable_entries/', views.display_timetable_entries, name='display_timetable_entries'),
    path('holidays/', views.display_holidays, name='display_holidays'),
    path('logout/', auth_views.LoginView.as_view(template_name='login.html'), name='logout'),
    path('home/', views.home, name='home'),
    path('create_teacher/', views.create_teacher, name='create_teacher'),
    path('create_student/', views.create_student, name='create_student'),
    path('create_holiday/', views.create_holiday, name='create_holiday'),
    path('create_room/', views.create_room, name='create_room'),
    path('create_course/', views.create_course, name='create_course'),

    # For Linking of every page
    path('details/<int:user_id>', views.details, name='details'),

    path('login/', views.login_view, name='login'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('create_class/', views.create_class, name='create_class'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    #path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('student/', views.student_dashboard, name='student_dashboard')
]


