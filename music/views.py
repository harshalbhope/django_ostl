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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book, Book_Format
from .forms import BookForm, Book_FormatForm, UserForm


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        books = Book.objects.filter(user=request.user)
        audio_results = Book_Format.objects.all()
        query = request.GET.get("q")
        if query:
            books = books.filter(
                Q(Book_title__icontains=query) |
                Q(Author__icontains=query)
            ).distinct()
            audio_results = audio_results.filter(
                Q(AUDIO_FILE__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'books': books ,
                'book_formats': audio_results,
            })
        else:
            return render(request, 'music/index.html', {'books': books})



def detail(request, book_id):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        user = request.user
        books = get_object_or_404(Book, pk=book_id)
        return render(request, 'music/detail.html', {'book': books, 'user': user})


def create_book(request):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.Book_logo = request.FILES['Book_logo']
            file_type = book.Book_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'book': book,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/create_book.html', context)
            book.save()
            return render(request, 'music/detail.html', {'book': book})
        context = {
            "form": form,
        }
        return render(request, 'music/create_book.html', context)

def create_audio(request, book_id):
    form = Book_FormatForm(request.POST or None, request.FILES or None)
    book = get_object_or_404(Book, pk=book_id)
    if form.is_valid():
        books_audio = book.book_format_set.all()
        for s in books_audio:
            if s.Audio_title == form.cleaned_data.get("Audio_title"):
                context = {
                    'book': book,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.book = book
        song.Audio = request.FILES['Audio']
        file_type = song.Audio.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'book': book,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/detail.html', {'book': book})
    context = {
        'book': book,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)

def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    books = Book.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'books': books})

def favorite_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        if book.is_favorite:
            book.is_favorite = False
        else:
            book.is_favorite = True
            book.save()
    except (KeyError, Book.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'books': books})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
         "form": form,
    }
    return render(request, 'music/login.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'Book': books})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)

def delete_audio(request, book_id, audio_id):

     book = get_object_or_404(Book, pk=book_id)
     audio = Book_Format.objects.get(pk=audio_id)
     audio.delete()
     return render(request, 'music/detail.html', {'Book': book})



def favorite(request, audio_id):
    audio = get_object_or_404(Book_Format, pk=audio_id)
    try:
        if audio.is_favorite:
            audio.is_favorite = False
        else:
            audio.is_favorite = True
        audio.save()
    except (KeyError, Book_Format.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def audios(request, filter_by):
    if not request.user.is_authenticated:
        return render(request, 'music/login.html')
    else:
        try:
            audio_ids = []
            for book in Book.objects.filter(user=request.user):
                for song in book.book_format_set.all():
                    audio_ids.append(song.pk)
            users_songs = Book_Format.objects.filter(pk__in=audio_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Book.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'audio_list': users_songs,
            'filter_by': filter_by,
        })
