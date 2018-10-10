from django.db import models

class Url(models.Model):
    long_url = models.CharField(max_length=500)
    short_url = models.CharField(max_length=200)

    def __str__(self):
        return self.short_url