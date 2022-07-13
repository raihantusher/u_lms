from django.shortcuts import render
from .models import BookStudent


# Create your views here.


def home(request):
    return render(request, 'student/portal.html')


def issued_book(request):
    issued_book = BookStudent.objects.filter(
        student=request.user.student
    ).all().order_by('-id')

    context = {
        'issued_books': issued_book
    }
    return render(request, 'student/issued.html', context)
