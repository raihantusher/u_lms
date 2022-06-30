from django.contrib import admin

# Register your models here.
from student.models  import Department, Student, Book_Student


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Book_Student)