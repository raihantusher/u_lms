from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'backend/dashboard.html')


# cat operation starts here

def list_category(request):
    return render(request, 'backend/category/list.html')


def add_category(request):
    return render(request, 'backend/category/add.html')


def edit_category(request):
    return render(request, 'backend/category/add.html')


def del_category(request, id):
    return render(request, 'uc.html')


# cat operation ends here


# cat operation starts here

def list_book(request):
    return render(request, 'backend/book/list.html')


def add_book(request):
    return render(request, 'backend/book/add.html')


def edit_book(request, id):
    return render(request, 'backend/book/add.html')


def del_book(request, id):
    return render(request, 'uc.html')


# cat operation ends here


# cat operation starts here

def list_dept(request):
    return render(request, 'backend/dept/list.html')


def add_dept(request):
    return render(request, 'backend/dept/add.html')


def edit_dept(request):
    return render(request, 'backend/dept/add.html')


def del_dept(request, id):
    return render(request, 'uc.html')

# cat operation ends here
