from django.db import models


class GameRecord(models.Model):
    winner = models.CharField(max_length=200)


