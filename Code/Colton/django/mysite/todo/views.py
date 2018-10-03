from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Add


def index(request):
    todos = Add.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def addtodo(request):
    todo = request.POST['todo']

    todo.save()

def deletecontact(request):
    id = request.POST['id']
    todo = Todo.objects.get(pk=id)
    Todo.delete()

    return HttpResponseRedirect(reverse('todo:index'))