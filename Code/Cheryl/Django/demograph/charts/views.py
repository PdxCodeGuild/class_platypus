
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils import timezone
from .models import IncomeData, Gender, EducationLevel



def index(request):
    return render(request, 'charts/index.html', {})


def getdata(request):
    # items = IncomeData.objects.filter(year='2015', gender=Gender.objects.get(pk=2), education_level=EducationLevel.objects.get(pk=1))
    items = IncomeData.objects.filter(year='2015')

    return render(request, 'charts/graphs.html', {'items': items})
