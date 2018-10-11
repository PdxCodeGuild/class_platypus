from django.db import models

class PlatformType(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField()

    def __str__(self):
        return self.name

class Platform(models.Model):
    platform_type = models.ForeignKey(PlatformType, on_delete=models.PROTECT)
    username = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.username
