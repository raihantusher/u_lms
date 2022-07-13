from django.shortcuts import render
from django.http import HttpResponseRedirect

from book.models import Book
from student.models import Book_Student


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
        book = Book.objects.filter(pk=id, available=True).last()
        # print(request.POST.get('book_id'))
        context = {
            'book': book
        }

        return render(request, 'frontend/request_success.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def advertisment(request):
    return HttpResponseRedirect("https://crowdfire.grsm.io/o0fqs0u2n22f")
