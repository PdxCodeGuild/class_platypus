from django.db import models


class ShortUrl(models.Model):
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.code


class UserUrl(models.Model):
    original_url = models.CharField(max_length=100)

    def __str__(self):
        return self.original_url