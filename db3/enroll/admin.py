from django.contrib import admin
from .models import Student
# Register your models here.

# using decorator
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuId','stuName','stuEmail','stuPass')



# admin.site.register(Student,StudentAdmin)
