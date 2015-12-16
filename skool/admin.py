from django.contrib import admin
from skool.models import Department, Faculty, Student, UserProfile

# Register your models here.


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'DOJ']
    ordering = ['DOJ']
    #actions = [make_published]
    search_fields = ['name']

class StudentAdmin(admin.ModelAdmin):
	list_display = ['roll_no', 'first_name', 'standard','email']
	ordering = ['roll_no']
	search_fields = ['first_name','roll_no']

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name', 'code', 'HOD']

class UserProfileAdmin(admin.ModelAdmin):
	search_fields = ['user__username']
	list_display = ['user', 'is_student', 'is_faculty']
	ordering = ['is_student','is_faculty']


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student,StudentAdmin)
