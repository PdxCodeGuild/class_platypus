from django.shortcuts import render, reverse


from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Todolist, TodoListItem




def index(request):
    lists = Todolist.objects.all()
    print(lists)
    return render(request, 'todo/index.html', {'lists': lists})


def detail(request, pk):

    if request.method == 'POST':
        if 'text' in request.POST:         # <--- add new item
            text = request.POST['text']
            item = TodoListItem(text=text, todolist_id=pk)
            item.save()
        else:
            id = request.POST['id']
            item = TodoListItem.objects.get(pk=id)
            item.completed_date = timezone.now()
            item.save()

    list = Todolist.objects.get(pk=pk)

    return render(request, 'todo/detail.html', {'list': list})

def all(request):
    pass

def add_todo(request):
    newtodo = request.POST['newtodo']
    print(newtodo)
    new_item = TodoListItem(text=newtodo, todolist_id=1)
    new_item.save()
    return HttpResponseRedirect(reverse('todo:index'))

def deletetodo(request):
    deletetodo = request.POST['id']
    print(deletetodo)
    delete_item = TodoListItem.objects.get(pk=deletetodo)
    delete_item.delete()
    return HttpResponseRedirect(reverse('todo:index'))

def completetodo(request):
    completetodo = request.POST['id']
    complete_todo = TodoListItem.objects.get(pk=completetodo)
    complete_todo.completed = True
    complete_todo.save()
    return HttpResponseRedirect(reverse('todo:index'))
