from django.db import models

from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

    def author_names(self):
        return ', '.join([author.name for author in self.authors.all()])

    def count_checkouts(self):
        return self.checkouts.all().count()


class BookCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='checkouts')
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkouts')
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ' - ' + self.book.title










