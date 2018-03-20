from django.db import models
from django.urls import reverse


class Book(models.Model):
    Author = models.CharField(max_length=250)
    Book_title = models.CharField(max_length=250)
    Typegenre = models.CharField(max_length=100)
    Book_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.Author + '-' + self.Book_title

# Create your models here.
class Book_Format(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Book_year = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.Publisher