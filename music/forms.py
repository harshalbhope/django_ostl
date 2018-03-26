from django.contrib.auth.models import User
from django import forms
from .models import Book, Book_Format

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['Book_title', 'Typegenre', 'Author', 'Book_logo']


class Book_FormatForm(forms.ModelForm):

    class Meta:
        model = Book_Format
        fields = ['Book_year', 'Publisher']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

