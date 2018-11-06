from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Color, TVShow, Person
import json

def index(request):
	colors = Color.objects.all()
	shows = TVShow.objects.all()
	return render(request, 'my_example/index.html', {'colors': colors, 'shows': shows})

def json_post(request):
	print(request)
	data = json.loads(request.body)
	show_obj = TVShow.objects.get(pk=data['show'])
	color_obj = Color.objects.get(pk=data['color'])
	people = Person.objects.all()
	print(f"all people {people}")
	if show_obj != None:
		people = people.filter(fav_tv=show_obj)
	print(f"after first filter {people}")
	if color_obj != None:
		people = people.filter(fav_color=color_obj)
	print(f"after second filter {people}")
	data = {'people': []}
	for person in people:
	    data['people'].append({'name': person.name})
	return JsonResponse(data)


	
