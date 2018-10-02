from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'todo/index.html', {})

def add(request):
    # receive the post request from the form in the template
    if request.POST['add_item'] == True:
        print('if working')
    else:
        print('else workign')
    print(request.POST['add_item'])
    return HttpResponse('ok')