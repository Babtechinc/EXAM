from django.db import models
from courseDetail.models import CourseInfo
from account.models import StudentDB,semester

# Create your models here.
class TakeAttendance(models.Model):
    CourseCode=models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    Student=models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Week =models.IntegerField(max_length=20,default=1)
    Semester = models.CharField(default="1", choices=semester, max_length=34)
    Date = models.DateTimeField()


class StudentTakeAttendance(models.Model):
    CourseCode=models.ForeignKey(CourseInfo, on_delete=models.CASCADE)
    Student=models.ForeignKey(StudentDB, on_delete=models.CASCADE)
    Week =models.IntegerField(max_length=20,default=1)
    Semester = models.CharField(default="1", choices=semester, max_length=34)
    Date = models.DateTimeField()
    def __str__(self):
        return self.Student