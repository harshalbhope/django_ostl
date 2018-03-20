from music import views
from django.urls import path
app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),
    #/music/register
    path('register/', views.UserFormView.as_view(), name='register'),
    #/music/<book_id>
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #/music/book/add/
    path('book/add/',views.BookCreate.as_view(),name='book-add'),
    #/music/book/2/
    path('book/<int:pk>/',views.BookUpdate.as_view(),name='book-update'),
    #/music/book/2/delete/
    path('book/<int:pk>/delete/',views.BookDelete.as_view(),name='book-delete'),
]