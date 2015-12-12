from django.contrib import admin
from skool.models import Department, Faculty, Student, UserProfile

# Register your models here.


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'DOJ']
    ordering = ['DOJ']
    #actions = [make_published]
    search_fields = ['name']

admin.site.register(UserProfile)
admin.site.register(Department)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student)
