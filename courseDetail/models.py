from django.db import models
from account.models import StudentDB,course,level,TeacherDB,semester
# Create your models here.

class CourseInfo(models.Model):
    CourseCode = models.CharField(max_length=11)
    CourseName = models.CharField(max_length=120)
    Courses = models.CharField(default="computer science",choices=course,max_length=34)
    level = models.CharField(default="student", choices=level, max_length=34)
    semester = models.CharField(default="1", choices=semester , max_length=34)

    def __str__(self):
        return self.CourseCode

class CourseRegister(models.Model):
    CourseCode = models.ForeignKey(CourseInfo,on_delete=models.CASCADE)
    Student = models.ForeignKey(StudentDB,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Student)

class CourseTeach(models.Model):
    CourseCode = models.ForeignKey(CourseInfo,on_delete=models.CASCADE)
    Teacher = models.ForeignKey(TeacherDB,on_delete=models.CASCADE,default="")

    def __str__(self):
        return str(self.Teacher)