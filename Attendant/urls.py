from django.urls import path
from Attendant import views

urlpatterns = [
path('Teacher/<str:course>',views.CourseAttendanceWeek, name='CourseAttendanceWeek'),
path('Teacher/AttendanceSubmited/<str:course>/week<int:week>',views.CourseAttendanceSubmited, name='CourseAttendanceSubmited'),
path('Teacher/Attendance/<str:course>/week<int:week>',views.CourseAttendance, name='CourseAttendance'),
path('Student/StudentAttendanceWeek/<str:course>',views.StudentAttendanceWeek, name='StudentAttendanceWeek'),
path('Student/StudentAttendanceWeek/<str:course>/week<int:week>',views.StudentAttendanceSubmit, name='StudentAttendanceSubmit'),
path('Student/StudentAttendedWeek/<str:course>/',views.StudentAttendanceSubmited, name='StudentAttendanceSubmited'),

# path('Student/StudentAttendanceWeekSubmited/<str:course>/week<int:week>',views.StudentAttendanceSubmited, name='StudentAttendanceSubmited'),
]