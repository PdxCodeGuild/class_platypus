from django.db import models

# Create your models here.


class Todolist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TodoListItem(models.Model):
    text = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='items')


    def __str__(self):
        return self.text