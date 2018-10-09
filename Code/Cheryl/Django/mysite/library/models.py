
from django.db import models
import datetime
from django.utils import timezone


class Book(models.Model):
    book_name = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name



class Author(models.Model):
    author_name = models.CharField(max_length=200)

    def __str__(self):
        return self.author_name


# class User(models.Model):
#     user_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.user_name
