from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(models.Model):

    user_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fee_balance = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', default='avatars/avatar.svg')
    dom = models.CharField(max_length=100, null=True, blank=True)
    room_no = models.CharField(max_length=100, null=True, blank=True )
    parents_phone = models.CharField(max_length=100, null=True, blank=True)
    parents_name = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    club = models.CharField(max_length=100, null=True, blank=True)
    

    def  __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField()


    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()

    class Meta:
        unique_together = ('student', 'course') 