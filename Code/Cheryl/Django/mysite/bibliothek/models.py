
import datetime

from django.db import models
from django.utils import timezone



class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Author(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)