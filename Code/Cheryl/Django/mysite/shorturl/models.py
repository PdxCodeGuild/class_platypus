from django.db import models


class ShortUrl(models.Model):
    user_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


