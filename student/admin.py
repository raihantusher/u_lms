from django.contrib import admin

# Register your models here.
from student.models  import Department, Student, BookStudent


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(BookStudent)