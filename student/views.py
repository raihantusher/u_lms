from django.shortcuts import render
from .models import BookStudent
from book.models import Book

# Create your views here.


def home(request):
    not_returned = BookStudent.objects.filter(student=request.user.student,  is_returned=False).count()
    total_books = Book.objects.all().count()

    context = {
        'not_returned':not_returned,
        'total_books':total_books
    }
    return render(request, 'student/portal.html', context)


def issued_book(request):
    issued_book = BookStudent.objects.filter(
        student=request.user.student
    ).all().order_by('-id')

    context = {
        'issued_books': issued_book
    }
    return render(request, 'student/issued.html', context)
