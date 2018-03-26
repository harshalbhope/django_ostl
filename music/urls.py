from music import views
from django.urls import path
app_name = 'music'

urlpatterns = [
    #/music/
    path('', views.index, name='index'),
    #/music/login_use
    path('login_user/',views.login_user,name='login_user'),
    #/music/logout_user
    path('logout_user/', views.logout_user, name='logout_user'),
    #/music/register
    path('register/', views.register, name='register'),


    #/music/<book_id>
    path('<int:book_id>/', views.detail, name='detail'),
    path('<int:audio_id>/favorite/', views.favorite, name='favorite'),


    # path('songs/<char:filter_by>/', views.audios, name='audios'),
    path('<int:book_id>/create_audio/', views.create_audio, name='create_audio'),
    path('<int:book_id>/delete_audio/<int:audio_id>', views.delete_audio, name='delete_audio'),

    path('create_book/', views.create_book, name='create_book'),
    path('<int:book_id>/favorite_book/', views.favorite_book, name='favorite_book'),
    path('<int:book_id>/delete_book/', views.delete_book, name='delete_book'),

]
