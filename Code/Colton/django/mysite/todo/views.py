from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Add


def index(request):
    todos = Add.objects.order_by('is_done')
    #is_done = Add.objects.filter(is_done=False)
    return render(request, 'todo/index.html', {'todos': todos})


def addtodo(request):
    thing = request.POST['thing']
    todo = Add(thing=thing)
    todo.save()
    return HttpResponseRedirect(reverse('todo:index'))


def deletetodo(request):
    complete = request.POST['id']
    complete = Add.objects.get(pk=complete)
    complete.is_done = True
    # is_done = Add(is_done=True)
    complete.save()
    return HttpResponseRedirect(reverse('todo:index'))


def clear_todo_list(request):
    delete = Add.objects.all().delete()
    return HttpResponseRedirect(reverse('todo:index'))
