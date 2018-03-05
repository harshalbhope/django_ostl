from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>thos ososo</h1>")

def detail(request,Book_id):
    return HttpResponse("<h2>details for book_id:"+ str(Book_id)+"</h2>")