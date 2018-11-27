from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class TVShow(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=127)
    fav_color = models.ForeignKey(Color, on_delete=models.PROTECT)
    fav_tv = models.ForeignKey(TVShow, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} likes {self.fav_color} and {self.fav_tv}"

# Create your models here.
