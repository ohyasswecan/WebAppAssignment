from django.contrib import admin

from gradebook import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.Lecturer)
admin.site.register(models.Semester)
admin.site.register(models.Class_Enrollment)
admin.site.register(models.Student_Enrollment)
