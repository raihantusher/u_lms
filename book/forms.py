from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book


class CatForm(forms.ModelForm):
    class Meta:
        model = Category
