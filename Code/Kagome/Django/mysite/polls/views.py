from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    # return HttpResponse("Making Thangs and Stuff.")
    return render(request, 'polls/index.html')



