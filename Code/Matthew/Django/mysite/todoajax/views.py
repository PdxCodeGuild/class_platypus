from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import  reverse

from .models import TodoAjaxItem

import json

def index(request):
    return render(request, 'todoajax/index.html', {})

def index2(request):
    return render(request, 'todoajax/index2.html', {})


def additem(request):
    data = json.loads(request.body)
    text = data['text']
    item = TodoAjaxItem(text=text)
    item.save()
    return HttpResponse('ok')

def getitems(request):
    items = TodoAjaxItem.objects.all()
    data = {'items': []}
    for item in items:
        data['items'].append({'text': item.text})
    return JsonResponse(data)



