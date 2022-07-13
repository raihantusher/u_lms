from django.db import models

from book.models import Book
from accounts.models import Account


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=150)
    student_id = models.CharField(max_length=150)
    department = models.ForeignKey(Department, related_name="students", on_delete=models.CASCADE)
    account = models.OneToOneField(Account, related_name='student', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book_Student(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Book n Student"
        verbose_name_plural = "Books n Students"

    def __str__(self):
        return self.student.student_id + ' ' + self.book.name
