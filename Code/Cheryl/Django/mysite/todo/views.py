from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import TodoItem


def index(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})


def add(request):
    # receive the post request from the form in the template
    todo_text = request.POST['TodoItem']
    todo_item = TodoItem(name=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

