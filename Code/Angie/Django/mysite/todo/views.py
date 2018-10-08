from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem


def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'message': 'To Do List', 'todos': todos})

# create item/add to list
def addItem(request):
    text = request.POST['text']
    # create an instance of the model specifying text and created date
    todo_item = TodoItem(text=text, created_date=timezone.now(), completed_date=None)
    # save the instance
    todo_item.save()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('todo:index'))
    # return HttpResponse(todo_item)

# complete item
def completeItem(request, pk):
    if request.method == 'POST':
        if 'text' in request.POST: # adding a new item
            text = request.POST['text']
            item = TodoItem(text=text, todos=pk)
            item.save()
        else:
            id = request.POST['id']
            item = TodoItem.objects.get(pk=id)
            item.completed_date = timezone.now()
            item.save()

    # list = TodoItem.objects.get(pk=pk)

    # return render(request, 'todo/index.html', {'todo': todos})
    # text = request.POST['text']
    # todo_item = TodoItem.objects.get(pk=text)
    # todo_item.complete()
    # todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))
    # return HttpResponse(todo_item)
# take completed item off of list
# place item in completed list

def deleteItem(request):
    text = request.POST['text']
    todo_item = TodoItem.objects.get(pk=text)
    todo_item.remove()
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))


