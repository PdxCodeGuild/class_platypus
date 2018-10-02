import datetime

from django.db import models
from django.utils import timezone



class Item(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added', auto_now_add=True)


    def __str__(self):
        return self.text

