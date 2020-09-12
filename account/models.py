from django.db import models
from django.contrib.auth.models import User

course = {
    ('CS', 'computer science'),
    ('MHE', 'mechnical engineering'),
    ('PS', 'political science'),
}
role = {
        ('teacher', 'teacher'),
        ('student', 'student')
    }
semester ={
        ('1', '1'),
        ('2', '2')
    }
level = {
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),}
# Create your models here.
class profile(models.Model):


    profileImg=models.ImageField(upload_to='profile_img/%Y/%m/%d/', blank=True)
    roleUser = models.CharField(default="student",choices=role,max_length=34)
    profileUser=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = [('can_eat_pizzas', 'Can eat pizzas')]


class StudentDB(models.Model):
    StudentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    StudentID = models.CharField(max_length=30,default="")
    StudentFname = models.CharField(max_length=30)
    StudentSname = models.CharField(max_length=30)
    level = models.CharField(default="student",choices=level,max_length=34)
    semester = models.CharField(default="1", choices=semester, max_length=34)
    StudentCourse = models.CharField(default="computer science",choices=course,max_length=34)
    def __str__(self):
        return self.StudentID

class TeacherDB(models.Model):
    TeacherId = models.CharField(max_length=30,default="")
    TeacherUser = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    TeacherFname = models.CharField(max_length=30,null=True)
    TeacherSname = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.TeacherId