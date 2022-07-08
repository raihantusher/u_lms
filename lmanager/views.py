from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from student.models import Department, Student
from book.models import Book, Category

from student.forms import DeptForm
from book.forms import BookForm, CatForm


# Create your views here.

def home(request):
    return render(request, 'backend/dashboard.html')


# cat operation starts here

def list_category(request):
    cats = Category.objects.all()
    context = {
        'all_categories': cats
    }
    return render(request, 'backend/category/list.html', context)


def add_category(request):
    cat_form = CatForm()

    if request.method == "POST":
        cat_form = CatForm(request.POST, request.FILES)
        if cat_form.is_valid():
            cat_form.save()
            messages.success(request, ' Category is created successfully!')
            redirect('list_cat')

    context = {
        'category_form': cat_form
    }

    return render(request, 'backend/category/add.html', context)


def edit_category(request, id):
    category = Category.objects.get(pk=id)
    category_form = CatForm(instance=category)

    if request.method == "POST":
        category_form = CatForm(instance=category, data=request.POST, files=request.FILES)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, f'category is updated successfully!')
            redirect('category_list')

    context = {
        'category_form': category_form,
        'category': category
    }
    return render(request, 'backend/category/add.html', context)


def del_category(request, id):
    if request.method == "POST":
        cat = Category.objects.get(pk=id)
        cat.delete()
        messages.success(request, f'Category is deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# cat operation ends here


# cat operation starts here

def list_book(request):
    books = Book.objects.all()
    context = {
        'all_books': books
    }
    return render(request, 'backend/book/list.html', context)


def add_book(request):
    book_form = BookForm()

    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)
        if book_form.is_valid():
            book_form.save()
            messages.success(request, ' Category is created successfully!')
            redirect('list_cat')

    context = {
        'book_form': book_form
    }
    return render(request, 'backend/book/add.html')


def edit_book(request, id):
    book = Book.objects.get(pk=id)
    book_form = BookForm(instance=book)

    if request.method == "POST":
        book_form = BookForm(instance=book, data=request.POST, files=request.FILES)
        if book_form.is_valid():
            book_form.save()
            messages.success(request, f'Book is updated successfully!')
            redirect('list_book')

    context = {
        'book_form': book_form,
        'book': book
    }
    return render(request, 'backend/book/add.html', context)


def del_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(pk=id)
        book.delete()
        messages.success(request, f'Book is deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# cat operation ends here










# department operation starts here

def list_dept(request):
    depts = Department.objects.all()
    context = {
        'all_depts': depts
    }
    return render(request, 'backend/dept/list.html', context)


def add_dept(request):
    dept_form = DeptForm()

    if request.method == "POST":
        dept_form = DeptForm(request.POST, request.FILES)
        if dept_form.is_valid():
            dept_form.save()
            messages.success(request, ' Category is created successfully!')
            redirect('list_dept')

    context = {
        'dept_form': dept_form
    }
    return render(request, 'backend/dept/add.html', context)


def edit_dept(request, id):
    dept = Department.objects.get(pk=id)
    dept_form = DeptForm(instance=dept)

    if request.method == "POST":
        dept_form = CatForm(instance=dept, data=request.POST, files=request.FILES)
        if dept_form.is_valid():
            dept_form.save()
            messages.success(request, f'Department is updated successfully!')
            redirect('list_dept')

    context = {
        'dept_form': dept_form,
        'dept': dept
    }
    return render(request, 'backend/dept/add.html')


def del_dept(request, id):
    if request.method == "POST":
        dept = Department.objects.get(pk=id)
        dept.delete()
        messages.success(request, f'Department is deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# cat operation ends here
