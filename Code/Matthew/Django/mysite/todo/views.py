from django.shortcuts import render


from django.http import HttpResponse
from django.utils import timezone
from .models import TodoList, TodoListItem




def index(request):
    lists = TodoList.objects.all()
    return render(request, 'todo/index.html', {'lists': lists})


def detail(request, pk):

    if request.method == 'POST':
        if 'text' in request.POST: # adding a new item
            text = request.POST['text']
            item = TodoListItem(text=text, todolist_id=pk)
            item.save()
        else:
            id = request.POST['id']
            item = TodoListItem.objects.get(pk=id)
            item.completed_date = timezone.now()
            item.save()

    list = TodoList.objects.get(pk=pk)

    return render(request, 'todo/detail.html', {'list': list})



def all(request):

    # grocery_list = TodoList.objects.get(name='grocery list') # get a row
    # items = grocery_list.todolistitem_set.all() # without related name
    # items = grocery_list.items.all() # with related name
    #
    # todo_lists = TodoList.objects.all()
    # for todo_list in todo_lists:
    #     print(todo_list.name)
    #     for todo_item in todo_list.todolistitem_set.all():
    #         print('\t' + todo_item.text)
    #
    #     # todo_items = TodoListItem.objects.filter(todolist_id=todo_list.id)

    lists = TodoList.objects.all()

    return render(request, 'todo/all.html', {'lists': lists})

