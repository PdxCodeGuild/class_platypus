
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel
import json
from django.http import JsonResponse




def index(request):
    # items = IncomeData.objects.filter(year='2015', gender=Gender.objects.get(pk=2), education_level=EducationLevel.objects.get(pk=1))
    items = IncomeData.objects.filter(year=2015)

    return render(request, 'charts/graphs.html', {'items': items})



def get_data(request):

    # items = IncomeData.objects.all()
    # items = IncomeData.objects.filter(year=2015)[:100]
    # data = []
    # for item in items:
    #      data.append({'gender': item.gender.name})
    # return JsonResponse({'data': data})

    # This allows you to see the specific json requested by putting in http://localhost:8000/get_data/?gender=Male
    gender = Gender.objects.get(name=request.GET['gender'])
    items = IncomeData.objects.filter(gender_id=gender.id)[:100]
    data = []
    for item in items:
         data.append({'gender': item.gender.name})
    return JsonResponse({'data': data})

def gender(request):
    pass


