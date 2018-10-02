from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
# Create your views here.
from .models import TodoItem

def index(request):
    todo = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo': todo})
def add(request):
    # receive the post request from the form in the template
    todo_text = request.POST['TodoItem']
    todo_item = TodoItem(name=todo_text)
    todo_item.save()
    return HttpResponseRedirect(reverse('todo:index'))