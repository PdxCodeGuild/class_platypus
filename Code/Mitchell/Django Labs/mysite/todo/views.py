from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Item

def index(request):
    todos = Item.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def addItem(request):
    new_item = request.POST['new_item']
    item = Item(text=new_item)
    item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def deleteItem(request):
    id = request.POST['id']
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('todo:index'))
