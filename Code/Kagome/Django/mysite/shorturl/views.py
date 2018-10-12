from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("URL Shortener!")

# Create your views here.

