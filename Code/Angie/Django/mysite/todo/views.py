from django.shortcuts import render


from django.http import HttpResponse
from .models import TodoItem


def index(request):
    todo = TodoItem.objects.all()
    return render(request, 'todo/index.html', {'todo': todo})

# create item
def addItem(request):
    text = request.POST['text']
# add item to list

# complete item
def completeItem(request):

# take completed item off of list
# place item in completed list

def deleteItem(request):


