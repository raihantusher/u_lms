from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'student/portal.html')


def issued_book(request):
    return render(request, 'student/issued.html')