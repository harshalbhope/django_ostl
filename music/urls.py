from music import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),

]