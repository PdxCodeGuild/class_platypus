import datetime
from django.db import models
from django.utils import timezone


class Add(models.Model):
    thing = models.CharField(max_length=200)
    add_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.thing



