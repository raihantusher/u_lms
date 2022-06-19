from django.db import models

from book.models import Book


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=150)


class Student(models.Model):
    name = models.CharField(max_length=150)
    student_id = models.CharField(max_length=150)
    department = models.ForeignKey(Department, related_name="students", on_delete=models.CASCADE)


class Book_Student(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
