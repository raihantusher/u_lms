from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',  views.home, name="portal"),
    path('issued-books/',  views.issued_book, name="issued_books"),
]
