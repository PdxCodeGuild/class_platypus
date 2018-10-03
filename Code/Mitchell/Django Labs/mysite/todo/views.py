from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from .models import Item

def index(request):
    #return render(request, 'todo/index.html', {'todos': ['a', 'b', 'c']})
    todos = Item.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def addItem(request):
    new_item = request.POST['new_item']
    item = Item(text=new_item)
    item.save()
    return HttpResponseRedirect(reverse('todo:index'))