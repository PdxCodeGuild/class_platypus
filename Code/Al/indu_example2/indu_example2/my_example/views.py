from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Grade
import json

def index(request):
    grades = Grade.objects.all()
    return render(request, 'my_example/index.html', {'grades': grades})

def json_get(request):
	print(request)
	students = Student.objects.all()
	grade = request.GET.get('grade')
	print(grade)
	chosen_grade = Grade.objects.get(pk=grade)
#	if chosen_grade != '':
#		students = students.filter(grade=chosen_grade)
	
	data = {'grades': {}}
	for student in students:
		add_grade = True
		for grade in data['grades']:
			if student.grade.name == grade:
				add_grade = False
		if add_grade:
			data['grades'][student.grade.name] = [{'name': student.name, 'cards': student.pokemon_cards, 'friends': student.friends}]
		else:
			data['grades'][student.grade.name].append({'name': student.name, 'cards': student.pokemon_cards, 'friends': student.friends})
	print(data)
	return JsonResponse(data)



# Create your views here.
