from django.contrib import admin

# Register your models here.
from book.models import Category, Book

admin.site.register(Category)
admin.site.register(Book)