from django.conf.urls import url
from . import views

urlpatterns = [
    #/music/
    url(r'^$',views.index, name='index'),

    #/music/23/
    url(r'^(?P<Book_id>[0-9]+)/$',views.detail,name='detail'),
]