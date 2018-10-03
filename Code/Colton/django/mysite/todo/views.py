from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Add


def index(request):
    todos = Add.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})


def addtodo(request):
    thing = request.POST['thing']
    todo = Add(thing=thing)
    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))


def deletetodo(request):
    complete = request.POST['id']
    complete = Add.objects.get(pk=complete)
    complete.delete()
    Add.complete = True
    return HttpResponseRedirect(reverse('todo:index'))
