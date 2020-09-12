from django.urls import path
from . import views

urlpatterns = [
    path('CourseRegister',views.CourseReg, name='CourseRegister'),
    path('CourseSelect',views.CourseSelect, name='CourseSelect'),
    path('CourseList/<str:course>',views.CourseList, name='CourseList'),
    path('CourseSelect/StudentAttendance', views.CourseStudentAttendence, name='StudentAttendence'),

]