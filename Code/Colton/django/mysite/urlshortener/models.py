from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link
