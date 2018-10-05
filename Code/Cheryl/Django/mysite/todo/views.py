from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils import timezone
from .models import TodoItem


def index(request):
    todos = TodoItem.objects.filter(completed_date__isnull=True)
    completed_todos = TodoItem.objects.filter(completed_date__isnull=False)
    return render(request, 'todo/index.html', {'todos': todos, 'completed_todos': completed_todos})


def add(request):
    # receive the post request from the form in the template
    todo_text = request.POST['TodoItem']
    todo_item = TodoItem(name=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def deletetodo(request):
    id = request.POST['id']
    todo = TodoItem.objects.get(pk=id)
    todo.delete()

    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    id = request.POST['id']
    done_item = TodoItem.objects.get(pk=id)
    done_item.completed_date = timezone.now()
    done_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

