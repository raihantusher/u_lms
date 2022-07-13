from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from book.models import Book
from student.models import BookStudent


def Home(request):
    return render(request, 'frontend/home.html')


def Details(request, id):
    detail = Book.objects.get(pk=id)
    context = {
        'single_book': detail
    }
    return render(request, 'frontend/details.html', context)


def book_request(request, id):
    if request.method == "POST" and request.user.is_authenticated == True:
        book = Book.objects.filter(pk=id).last()
        student = request.user.student

        book_student = None
        if book.available:
            book_student = BookStudent.objects.filter(book=book, student=student).last()

            if book_student.is_returned == True:
                print("book student is returned ")
                BookStudent.objects.create(book=book, student=student)
            elif book_student.is_returned == False:
                pass
            else:
                print(" Book is not available")
                BookStudent.objects.create(book=book, student=student)

        # print(request.POST.get('book_id'))
        context = {
            'book': book
        }

        return render(request, 'frontend/request_success.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def advertisment(request):
    return HttpResponseRedirect("https://crowdfire.grsm.io/o0fqs0u2n22f")
