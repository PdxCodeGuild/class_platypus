from django.db import models

class Item(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateTimeField('date added', auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text

