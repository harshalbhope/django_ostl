from django.http import HttpResponse
from .models import Book
from django.shortcuts import render


def index(request):
    all_books = Book.objects.all()

    html = ''
    for books in all_books:
        path = '/music/'+str(books.id)+'/'
        html += '<a href ="'+path+'">'+books.Publisher+'</a><br>'
    return HttpResponse(html)

def detail(request, book_id):
    return HttpResponse("<h2>details for book_id:" + str(book_id) + "</h2>")
