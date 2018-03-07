from django.http import HttpResponse
from django.template import loader
from .models import Book

def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('')
    return HttpResponse('')

def detail(request, book_id):
    return HttpResponse("<h2>details for book_id:" + str(book_id) + "</h2>")
