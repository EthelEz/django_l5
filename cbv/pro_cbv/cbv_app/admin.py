from django.contrib import admin

# Register your models here.
from cbv_app.models import School, Student  #, Teacher, Course

admin.site.register(School)
admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(Course)
