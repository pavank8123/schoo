from django.contrib import admin
from skool.models import Department, Faculty, Student, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
