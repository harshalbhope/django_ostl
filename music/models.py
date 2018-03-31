from django.db import models
from django.contrib.auth.models import Permission, User
from django.urls import reverse


class Book(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, default=1)
    Author = models.CharField(max_length=250)
    Book_title = models.CharField(max_length=250)
    Typegenre = models.CharField(max_length=100)
    Book_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.Book_title + '-' + self.Author


# Create your models here.
class Book_Format(models.Model):
    book = models.ForeignKey(Book,on_delete = models.CASCADE,)
    Audio_title = models.CharField(max_length=100)
    Audio = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.Audio_title