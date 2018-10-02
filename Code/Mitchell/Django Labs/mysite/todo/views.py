from django.shortcuts import render
from django.http import HttpResponse
from tkinter import *


def index(request):
    #btn = Button(top, text="Click Me")
    # return HttpResponse("Hello, world. You're at the todo index.")
    return render(request, 'todo/index.html', {'todos': ['a', 'b', 'c']})
