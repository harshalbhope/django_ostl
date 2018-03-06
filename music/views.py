from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>thos ososo</h1>")


def detail(request, book_id):
    return HttpResponse("<h2>details for book_id:" + str(book_id) + "</h2>")
