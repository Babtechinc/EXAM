from .models import profile,TeacherDB,StudentDB
from courseDetail.models import CourseTeach,CourseRegister
from django.contrib.auth.decorators import login_required

def add_variable_to_context(request):
    CourseTeaching =""
    Sumbitdb=""
    if request.user.is_authenticated:
        if TeacherDB.objects.filter(TeacherUser=request.user):
            TeacherUser =TeacherDB.objects.get(TeacherUser=request.user)
            CourseTeaching = CourseTeach.objects.filter(Teacher=TeacherUser)
        elif StudentDB.objects.filter(StudentUser=request.user):
            StudentUser=StudentDB.objects.get(StudentUser=request.user)
            if CourseRegister.objects.filter(Student=StudentUser.id):
                Sumbitdb = CourseRegister.objects.filter(Student=StudentUser.id)


    return {
        'Cteach': CourseTeaching,
        'CourseTaking':Sumbitdb
    }