from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import random


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    print('123')
    fruits =['apple','pear','orange ']
    return render(request, 'polls/index.html',{'message':'hhh','fruits':fruits})



def viewa(request):
    return HttpResponse('view a')


def viewb(request):
    return HttpResponse('view b')


def viewc(request):
    return HttpResponse('view c')