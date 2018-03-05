from django.db import models

class Book(models.Model):
    Author = models.CharField(max_length=250)
    Publisher = models.CharField(max_length=250)
    Type = models.CharField(max_length=100)
    Book_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.Publisher+'-'+ self.Author
# Create your models here.
class Book_name(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    Book_year = models.CharField(max_length=100)
    file_type = models.CharField(max_length=250)