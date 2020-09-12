from django.shortcuts import render,redirect
from account.models import StudentDB,TeacherDB
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse
from .models import TakeAttendance
from courseDetail.models import CourseInfo,CourseRegister,CourseTeach

@login_required(login_url='/account/login')
def CourseAttendance(respond,course,week):
    semester = '1'

    print(respond.POST)
    Move = ""
    Sumbitdb = {}
    if TeacherDB.objects.filter(TeacherUser=respond.user):
        Teachcourse = TeacherDB.objects.get(TeacherUser=respond.user)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if not TakeAttendance.objects.filter(CourseCode=TeachcourseCode,Week=week):
            if CourseTeach.objects.filter(Teacher=Teachcourse.id, CourseCode =TeachcourseCode.id):
                if CourseInfo.objects.filter(CourseCode=course):
                    CCourse = CourseInfo.objects.get(CourseCode=course)
                    if CourseRegister.objects.filter(CourseCode=CCourse):
                        Sumbitdb = CourseRegister.objects.filter(CourseCode=CCourse)
                for hey in respond.POST:
                    if hey != "csrfmiddlewaretoken":
                        print(hey)
                        date = datetime.datetime.now()
                        print(date)
                        StudCourse = StudentDB.objects.get(StudentID=hey)
                        attendance =TakeAttendance.objects.create(CourseCode=TeachcourseCode,Week=week,Semester='1',Date=date,Student=StudCourse)
                        attendance.save()
                        Move='yes'

            else:
                return redirect("CourseSelect")
        else:
            return redirect("CourseAttendanceSubmited",course,week)
    else:
        return redirect("404")

    if Move == 'yes':
        return redirect("CourseAttendanceSubmited", course, week)
    return render(respond,"CourseAttendence.html",context={"Stud" : Sumbitdb,'course':course,'week':week})

@login_required(login_url='/account/login')
def CourseAttendanceSubmited(respond,course,week):
    semester = '1'

    print(respond.POST)
    Sumbitdb = {}
    Attendance={}
    NoAttendance = {}
    if TeacherDB.objects.filter(TeacherUser=respond.user):
        Teachcourse = TeacherDB.objects.get(TeacherUser=respond.user)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if TakeAttendance.objects.filter(CourseCode=TeachcourseCode, Week=week):
            if CourseTeach.objects.filter(Teacher=Teachcourse.id, CourseCode=TeachcourseCode.id):
                if CourseInfo.objects.filter(CourseCode=course):
                    CCourse = CourseInfo.objects.get(CourseCode=course)
                    if CourseRegister.objects.filter(CourseCode=CCourse):
                        Sumbitdb = CourseRegister.objects.filter(CourseCode=CCourse)
                        TakeAttendanceList = TakeAttendance.objects.filter(CourseCode=TeachcourseCode, Week=week,Semester=semester)
                        for foo in Sumbitdb:
                            for doo in TakeAttendanceList:
                                if foo.Student.StudentID==doo.Student.StudentID:
                                    Attendance.update({foo.Student.StudentID:'YES'})


                            if foo.Student.StudentID not in Attendance   :
                                    NoAttendance.update({foo.Student.StudentID: 'NO'})



            else:
                return redirect("CourseSelect")
        else:
           return  redirect("CourseAttendance",course,week)
    else:
        return redirect("404")
    print(Attendance)
    print(NoAttendance)
    return render(respond, "CourseAttendenceSubmit.html", context={"Stud": Sumbitdb, 'course': course, 'week': week,'NoTakeAttendanceList':NoAttendance,'TakeAttendanceList':Attendance})


login_required(login_url='/account/login')
def CourseAttendanceWeek(respond,course):
    print(respond.POST)
    if TeacherDB.objects.filter(TeacherUser=respond.user):
        Teachcourse = TeacherDB.objects.get(TeacherUser=respond.user)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if CourseTeach.objects.filter(Teacher=Teachcourse.id, CourseCode=TeachcourseCode.id):
            Sumbitdb = (1,2,3,4,5,6,7,8,9,10,11,12)

    else:
        return redirect("404")
    return render(respond,"CourseAttendenceWeek.html",context={"week" : Sumbitdb,'course':course})
def StudentAttendanceWeek(respond,course):
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if not TakeAttendance.objects.filter(CourseCode=TeachcourseCode, Student=StudCourse, Semester='1'):
            print(respond.POST)
            Sumbitdb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        else:
            return redirect("StudentAttendanceSubmited", course)
    else:
        return redirect("404")
    return render(respond, "StudentAttendenceWeek.html", context={"week": Sumbitdb, 'course': course})
def StudentAttendanceSubmit(respond,course,week):
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)

        print(respond.POST)
        Sumbitdb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if not TakeAttendance.objects.filter(CourseCode=TeachcourseCode,Week=week,Student=StudCourse,Semester='1'):
            if CourseInfo.objects.filter(CourseCode=course):
                CCourse = CourseInfo.objects.get(CourseCode=course)
                if CourseRegister.objects.filter(CourseCode=CCourse):
                    Sumbitdb = CourseRegister.objects.filter(CourseCode=CCourse)
            for hey in respond.POST:
                if hey != "csrfmiddlewaretoken":
                    print(hey)
                    date = datetime.datetime.now()
                    print(date)
                    attendance = TakeAttendance.objects.create(CourseCode=TeachcourseCode, Week=week, Semester='1',
                                                               Date=date, Student=StudCourse)
                    attendance.save()
                    Move = 'yes'
                    return redirect("StudentAttendanceSubmited", course)



            else:
                return redirect("CourseSelect")
        else:
            return redirect("StudentAttendanceSubmited",course)

    else:
        return redirect("404")

    print('3ewd')
    return render(respond,"CourseStudentAttendent.html",context={"week" : Sumbitdb,'course':course})
def StudentAttendanceSubmited(respond,course):
    Attendance = {}
    if StudentDB.objects.filter(StudentUser=respond.user):
        StudCourse = StudentDB.objects.get(StudentUser=respond.user)

        print(respond.POST)
        Sumbitdb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        TeachcourseCode = CourseInfo.objects.get(CourseCode=course)
        if TakeAttendance.objects.filter(CourseCode=TeachcourseCode,Student=StudCourse,Semester='1'):
            if CourseInfo.objects.filter(CourseCode=course):
                CCourse = CourseInfo.objects.get(CourseCode=course)
                if CourseRegister.objects.filter(CourseCode=CCourse):
                    print(respond.POST)
                    Sumbitdb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    for foo in Sumbitdb:
                        if TakeAttendance.objects.filter(CourseCode=TeachcourseCode,Week=foo,Student=StudCourse,Semester='1'):
                            Attendance.update({foo: 'YES'})
                        else:
                            Attendance.update({foo: 'NO'})






            else:
                return redirect("CourseSelect")
        else:
            return redirect("StudentAttendanceSubmit",course)

    else:
        return redirect("404")

    print(Attendance)
    return render(respond, "StudentAttendedWeek.html", context={"week": Attendance, 'course': course})