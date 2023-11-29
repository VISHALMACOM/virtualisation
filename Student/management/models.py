from django.db import models

# Create your models here.

# models.py

from django.db import models

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=15, primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length=30)
    course_credits = models.IntegerField()
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title

class Class(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_start_date = models.DateField()
    class_end_date = models.DateField()
    class_time = models.TimeField()

    def __str__(self):
        return self.class_name

class Student(models.Model):
    student_id = models.CharField(max_length=15, primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_num = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    user_role = models.CharField(max_length=30)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user_name} {self.password} {self.user_role}"

class Attendance(models.Model):
    attendance_id = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    attendance_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, default='ABSENT')

    def __str__(self):
        return f"{self.student_id} - {self.attendance_date}"

class TimeTable(models.Model):
    time_table_id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Time Table ID: {self.time_table_id} - Class ID: {self.class_id}"

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_name = models.CharField(max_length=6)
    room_building = models.CharField(max_length=3)

    def __str__(self):
        return f"Room ID: {self.room_id} - {self.room_name}"

class TimeTableEntry(models.Model):
    entry_id = models.IntegerField(primary_key=True)
    time_table_id = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Entry ID: {self.entry_id} - Time Table ID: {self.time_table_id}"

class Holiday(models.Model):
    holiday_id = models.IntegerField(primary_key=True)
    holiday_date = models.DateField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"Holiday ID: {self.holiday_id} - {self.description}"



