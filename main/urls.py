from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student-list'),  # URL pattern for the student list view
]
