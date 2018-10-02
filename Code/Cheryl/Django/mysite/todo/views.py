from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'todo/index.html', {})

def add(request):
    # receive the post request from the form in the template
    if request.POST['TodoItem'] == True:
        print('if working')
        name.save()
    else:
        print('else workign')
    print(request.POST['TodoItem'])
    return HttpResponse('ok')