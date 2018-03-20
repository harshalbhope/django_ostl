from django.shortcuts import render,get_object_or_404
from .models import Book,Book_Format


# def index(request):
#     all_books = Book.objects.all()
#     return render(request,'music/index.html',{'all_books' : all_books})
#
#
# def detail(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, 'music/detail.html', {'book' : book})
#
# def favorite(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     try:
#         selected_book = book.book_format_set.get(pk = request.POST['booky'])
#     except(KeyError, Book_Format.DoesNotExist):
#         return render(request,'music/detail.html', {'book' : book,'error_message':"unvalid book",})
#     else:
#         selected_book.is_favorite = True
#         selected_book.save()
#         return render(request, 'music/detail.html', {'book': book})

#  accepted
# You can use triple-quoted strings. When they're not a docstring (first thing in a class/function/module), they are ignored.

from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'music/detail.html'


class BookCreate(CreateView):
    model = Book
    fields = ['Author','Book_title','Typegenre','Book_logo']


class BookUpdate(UpdateView):
    model = Book
    fields = ['Author','Book_title','Typegenre','Book_logo']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display form data
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects id cewdwntials are correct
            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})