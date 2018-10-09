from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItem


def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'message': 'To Do List', 'todos': todos})


# add/complete item
def completeItem(request):
    if request.method == 'POST':
        if 'text' in request.POST: # adding a new item
            text = request.POST['text']
            todo_item = TodoItem(text=text, created_date=timezone.now())
            todo_item.save()
        else:
            id = request.POST['id']
            item = TodoItem.objects.get(pk=id)
            item.completed_date = timezone.now()
            item.save()
    return HttpResponseRedirect(reverse('todo:index'))



def deleteItem(request):
    id = request.POST['id']
    todo_item = TodoItem.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('todo:index'))


