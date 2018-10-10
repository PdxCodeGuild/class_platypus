from django.db import models

# Create your models here.


class Todolist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TodoListItem(models.Model):
    text = models.CharField(max_length=100)
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='items')

    def is_completed(self):
        return self.completed_date is not None

    def __str__(self):
        return self.text