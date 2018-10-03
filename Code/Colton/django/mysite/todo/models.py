
from django.db import models



class Add(models.Model):
    thing = models.CharField(max_length=200)

    def __str__(self):
        return self.todo_text


