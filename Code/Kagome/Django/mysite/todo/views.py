from django.shortcuts import render


from django.http import HttpResponse
from django.utils import timezone
from .models import Todolist, TodoListItem




def index(request):
    lists = Todolist.objects.all()
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