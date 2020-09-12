from django.contrib import admin
from account.models import StudentDB,profile,TeacherDB
# Register your models here.
admin.site.register(StudentDB)
admin.site.register(profile)
admin.site.register(TeacherDB)