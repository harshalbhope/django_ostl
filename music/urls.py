from django.conf.urls import url
from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
]