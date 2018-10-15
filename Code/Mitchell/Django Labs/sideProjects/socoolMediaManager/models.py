from django.db import models
from django.contrib.auth.models import User


class PlatformType(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.name

class Platform(models.Model):
    platform_type = models.ForeignKey(PlatformType, on_delete=models.PROTECT)
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.username
