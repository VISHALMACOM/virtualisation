from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
#from django.db.backends.sql import sql
from .models import Teacher, Course, Class, Student, Attendance, TimeTable, Room, TimeTableEntry, Holiday, Users
from django.contrib.auth import login, logout, authenticate

#conn = psycopg2.connect("dbname='postgres' user='postgres' host='postgres' password='postgres'")    


# Debugging Purpose
import inspect
class LineNo:
    def __str__(self):
        return str(inspect.currentframe().f_back.f_lineno)

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Vishal'})

def display_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def display_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def display_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def display_classes(request):
    classes = Class.objects.all()
    return render(request, 'classes.html', {'classes': classes})

def display_students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def display_attendance(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance.html', {'attendance_records': attendance_records})

def display_timetable(request):
    timetable_records = TimeTable.objects.all()
    return render(request, 'timetable.html', {'timetable_records': timetable_records})

def display_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def display_timetable_entries(request):
    timetable_entries = TimeTableEntry.objects.all()
    return render(request, 'timetable_entries.html', {'timetable_entries': timetable_entries})

def display_holidays(request):
    holidays = Holiday.objects.all()
    return render(request, 'holidays.html', {'holidays': holidays})

def custom_login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def create_teacher(request):
    if request.method == 'POST':
        teacher_id = request.POST.get('teacher_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Check if the teacher already exists
        existing_teacher = Teacher.objects.filter(teacher_id=teacher_id).first()

        if not existing_teacher:
            # Create a new Teacher object
            new_teacher = Teacher.objects.create(teacher_id=teacher_id, first_name=first_name, last_name=last_name)
        else:
            new_teacher = existing_teacher

        print(teacher_id, first_name, last_name)
        user_name = first_name + last_name[0]
        print(user_name)

        # Create a new User and associate it with the teacher
        Users.objects.create(user_name=user_name, password=user_name, user_role="T",
                             teacher_id=new_teacher, student_id=None)

        return redirect('display_teachers')
    return render(request, 'create_teacher.html')

def create_student(request):
    if request.method == 'POST':
        # Extract data from the POST request
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        roll_num = request.POST.get('roll_num')

        # Check if the teacher already exists
        existing_student = Student.objects.filter(student_id=student_id).first()

        if not existing_student:
            # Create a new Teacher object
            new_student = Student.objects.create(student_id=student_id, first_name=first_name, last_name=last_name, roll_num=roll_num)
        else:
            new_student = existing_student

        user_name = first_name + last_name[0]

        # Create a new User and associate it with the teacher
        Users.objects.create(user_name=user_name, password=user_name, user_role="S",
                             teacher_id=None, student_id=new_student)

        return redirect('display_students')
    return render(request, 'create_student.html')

def create_holiday(request):
    if request.method == 'POST':
        holiday_id = request.POST.get('holiday_id')
        holiday_date = request.POST.get('holiday_date')
        description = request.POST.get('description')
        Holiday.objects.create(holiday_id=holiday_id, holiday_date=holiday_date, description=description)
        return redirect('display_holidays')  # Redirect to the list of holidays page
    return render(request, 'create_holiday.html')

def create_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        room_name = request.POST.get('room_name')
        room_building = request.POST.get('room_building')
        Room.objects.create(room_id=room_id, room_name=room_name, room_building=room_building)
        return redirect('display_rooms')  # Redirect to the list of rooms page
    return render(request, 'create_room.html')

def create_course(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course_title = request.POST.get('course_title')
        course_credits = request.POST.get('course_credits')
        teacher_id = request.POST.get('teacher_id')

        # Check if teacher exists
        try:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
        except Teacher.DoesNotExist:
            return HttpResponse("Teacher does not exist")

        # Check if course exists
        if Course.objects.filter(course_id=course_id).exists():
            return HttpResponse("Course already exists")
        else:
            # Create the course if it doesn't exist
            course = Course(course_id=course_id, course_title=course_title, course_credits=course_credits, teacher_id=teacher)
            course.save()
            return HttpResponse("Course added successfully")

    return render(request, 'create_course.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        existing_user = Users.objects.filter(user_name=username).first()
        print("existing_user is ", existing_user)

        if not existing_user:
            # Print Error Message as not found
            return render(request, 'login.html')
        else:
            print("In else statement", existing_user.teacher_id)
            print("role is ", existing_user.user_role)
            print(type(existing_user.user_role))


            if existing_user.user_role == "T":
                return teacher_dashboard(request, existing_user.teacher_id)

            if existing_user.user_role == "S":
                #return HttpResponse(request, teacher_dashboard(request, existing_user.teacher_id))
                return student_dashboard(request, existing_user.student_id)

    return render(request, 'login.html')



def teacher_dashboard(request, teacher):
    print("teacher_id is ", teacher)

    # Assuming you retrieve the teacher based on some authentication or session information
    #teacher = Teacher.objects.get(teacher_id=teacher_id)  # Fetch the specific teacher

    context = {'teacher': teacher}
    return render(request, 'teacher_dashboard.html', context)

def create_class(request):
    classes = Class.objects.all()
    return render(request, 'create_class.html')

def student_dashboard(request, student):
    # Sample data for student's dashboard
    classes = Class.objects.all()  # Fetching all classes, you might need specific logic
    context = {'classes': classes}
    return render(request, 'student_dashboard.html', context)

def details(request, user_id):
    print("In details akddsfjkladskja")
    myuser = Users.objects.get(user_id=user_id)
    # Rest of your logic to fetch user details and render the details page
    template = loader.get_template('details.html')
    context = {
        'myuser': myuser,
    }
    return HttpResponse(template.render(context, request))
