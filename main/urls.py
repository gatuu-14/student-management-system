from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = 'home'),
    path("student_list", views.student_list, name= "student_list"),
    path("parent_detail", views.parent_detail, name="parent_detail"),
    path("enroll_student", views.enroll_student, name="enroll_student"),
     
    
]


