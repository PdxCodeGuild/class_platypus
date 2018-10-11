from django.db import models


# Create your models here.

class UrlShort(models.Model):
    long_url = models.CharField(max_length=200)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.code +  ' - ' + self.long_url

