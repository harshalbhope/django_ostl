from django.db import models

class Book(models.Model):
    Author = models.CharField(max_length=250)
    Book_title = models.CharField(max_length=250)
    Typegenre = models.CharField(max_length=100)
    Book_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.Author + '-' + self.Book_title
# Create your models here.


class Book_Format(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Book_year = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=250)

    def __str__(self):
        return self.Publisher