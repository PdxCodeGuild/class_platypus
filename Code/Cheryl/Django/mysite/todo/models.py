from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

# class TodoList(models.Model):


class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    completed_date = models.DateTimeField('date completed', null=True, blank=True)

    def __str__(self):
        return self.name

    def is_completed(self):
        return self.completed_date != None



