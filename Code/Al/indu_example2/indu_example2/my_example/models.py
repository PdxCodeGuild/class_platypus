from django.db import models

class Grade(models.Model):
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=127)
	pokemon_cards = models.IntegerField()
	friends = models.IntegerField()
	grade = models.ForeignKey(Grade, on_delete=models.PROTECT)

	def __str__(self):
		return self.name

# Create your models here.
