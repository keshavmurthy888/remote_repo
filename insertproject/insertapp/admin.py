from django.contrib import admin
from insertapp.models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('NAME','USN','PHONE_NUMBER','EMAIL','GENDER')
  

admin.site.register(Student_Detail, StudentAdmin)