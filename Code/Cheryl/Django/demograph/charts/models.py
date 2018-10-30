from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone


class EducationLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IncomeLevel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class IncomeData(models.Model):
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    income_level = models.ForeignKey(IncomeLevel, on_delete=models.CASCADE)
    population = models.IntegerField()
    year = models.IntegerField()
    county = models.CharField(max_length=100)

    def __str__(self):
        return self.education_level.name + ' - ' + self.gender.name + ' - ' + self.income_level.name + ' - ' + str(self.population) + ' - ' + str(self.year)


