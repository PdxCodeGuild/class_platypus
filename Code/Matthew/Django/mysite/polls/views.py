from django.shortcuts import render
from django.http import HttpResponse


import random

def index(request):

    # emojis = '😂🤣😃👋👴👵'
    # output = ''
    # for i in range(10000):
    #     output += random.choice(emojis)

    # fruits = ['apples', 'bananas', 'pears']
    # output = '<ul>'
    # for fruit in fruits:
    #     output += '<li>' + fruit + '</li>'
    # output += '</ul>'
    # return HttpResponse(output)

    # return HttpResponse('index view')

    # print('test123')
    # print(request.method)
    # print(request.GET['q'])
    #
    fruits = ['apples', 'bananas', 'pears', request.GET['q']]
    return render(request, 'polls/index.html', {'message': 'hello world!!', 'fruits': fruits})




def viewa(request):
    return HttpResponse('view a')

def viewb(request):
    return HttpResponse('view b')

def viewc(request):
    return HttpResponse('view c')
