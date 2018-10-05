from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Item

def index(request):
    uncompleted_todos = Item.objects.filter(completed=False)
    completed_todos = Item.objects.filter(completed=True)
    return render(request, 'todo/index.html', {'uncompleted_todos': uncompleted_todos, 'completed_todos': completed_todos})

def addItem(request):
    new_item = request.POST['new_item']
    item = Item(text=new_item)
    item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def completeItem(request):
    id = request.POST['id']
    complete = Item.objects.get(pk=id)
    complete.completed = True
    complete.save()
    return HttpResponseRedirect(reverse('todo:index'))

def deleteItem(request):
    id = request.POST['id']
    item = Item.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def clearItems(request):
    completed_todos = Item.objects.filter(completed=True)
    for completed_todo in completed_todos:
        completed_todo.delete()
    return HttpResponseRedirect(reverse('todo:index'))
