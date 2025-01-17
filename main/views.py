from django.shortcuts import render
from .models import Student

def student_list(request):
    # Fetch all students from the database
    students = Student.objects.all()
    
    # Render the 'student_list.html' template and pass the students list
    return render(request, 'student_list.html', {'students': students})
