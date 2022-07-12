from django.shortcuts import render
from django.http import HttpResponseRedirect

from book.models import Book

def Home(request):
    return render(request, 'frontend/home.html')


def Details(request, id):
    detail = Book.objects.get(pk=id)
    context = {
        'single_book': detail
    }
    return render(request, 'frontend/details.html', context)


def advertisment(request):
    return HttpResponseRedirect("https://crowdfire.grsm.io/o0fqs0u2n22f")
