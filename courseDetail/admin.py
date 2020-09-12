from django.contrib import admin
from .models import CourseInfo,CourseRegister,CourseTeach
# Register your models here.
admin.site.register(CourseInfo)
admin.site.register(CourseRegister)
admin.site.register(CourseTeach)