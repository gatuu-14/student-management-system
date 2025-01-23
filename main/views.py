from django.shortcuts import render,  get_object_or_404, redirect
from .models import *

def student_list(request):
    # Fetch all students from the database
    students = Student.objects.all()
    
    # Render the 'student_list.html' template and pass the students list
    return render(request, 'student_list.html', {'students': students})

def home(request):
    return render(request , 'home.html')

def index(request):
    return render(request , 'index.html')

def parent_detail(request, student_id):
    parent = get_object_or_404(parent, id=student_id)
    return render(request, 'parent_detail.html', {'parent': parent})


def enroll_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        Enrollment.objects.create(student=student, course=course, enrollment_date=request.POST.get('enrollment_date'))
        return redirect('student_detail', student_id=student.id)
    courses = Course.objects.all()
    return render(request, 'students/enroll_student.html', {'student': student, 'courses': courses})