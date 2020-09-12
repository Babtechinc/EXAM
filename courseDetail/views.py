from django.shortcuts import render,redirect
from .models import CourseInfo,CourseRegister,CourseTeach
from account.models import StudentDB,TeacherDB
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required(login_url='/account/login')
def CourseReg(respond):
    courseDB={}
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)

        if not CourseRegister.objects.filter(Student=StudCourse.id):
            if respond.POST.getlist('CourseSelect'):
                courseDB = CourseInfo.objects.filter(Courses=StudCourse.StudentCourse, level=StudCourse.level)
                for course in respond.POST.getlist('CourseSelect'):
                    CourseSumbit = CourseInfo.objects.get(id=course)
                    Sumbitdb = CourseRegister.objects.create(Student=StudCourse, CourseCode=CourseSumbit)
                    Sumbitdb.save()
                return redirect("CourseSelect")
            else:
                StudCourse = StudentDB.objects.get(StudentUser=respond.user)
                courseDB = CourseInfo.objects.filter(Courses=StudCourse.StudentCourse, level=StudCourse.level)
                messages.error(respond, 'Empty: SELECT YOUR COURSES')

        else:
          return redirect("CourseSelect")

    else:
        return redirect("404")
    return render(respond,'CourseRegister.html',context={'courseDB':courseDB})

@login_required(login_url='/account/login')
def CourseSelect(respond):

    Sumbitdb ={}
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)
        if CourseRegister.objects.filter(Student=StudCourse.id):
            Sumbitdb = CourseRegister.objects.filter(Student=StudCourse)
        else:
            return redirect("CourseRegister")
    else:
        return redirect("404")
    return render(respond, 'CourseSelect.html', context={"Sumbitdb":Sumbitdb})


@login_required(login_url='/account/login')
def CourseStudentAttendence(respond):
    Sumbitdb ={}
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)

        if CourseRegister.objects.filter(Student=StudCourse.id):
            Sumbitdb = CourseRegister.objects.filter(Student=StudCourse)
        else:
            return redirect("CourseRegister")
    else:
        return redirect("404")
    return render(respond, 'CourseStudentAttendent.html', context={"Sumbitdb":Sumbitdb})

@login_required(login_url='/account/login')
def CourseList(respond,course):

    Sumbitdb ={}
    if TeacherDB.objects.filter(TeacherUser=respond.user):
        Teachcourse = TeacherDB.objects.get(TeacherUser=respond.user)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if CourseTeach.objects.filter(Teacher=Teachcourse.id,CourseCode=TeachcourseCode.id):
            if CourseInfo.objects.filter(CourseCode=course):
                CCourse = CourseInfo.objects.get(CourseCode=course)
                if CourseRegister.objects.filter(CourseCode=CCourse):
                    Sumbitdb = CourseRegister.objects.filter(CourseCode=CCourse)
        else:
            return redirect("404")
    else:
        return redirect("404")
    # else:
    #     return redirect("CourseRegister")
    return render(respond, 'CourseList.html', context={"Sumbitdb":Sumbitdb})