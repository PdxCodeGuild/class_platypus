from django.shortcuts import render
from .models import Url

def index(request):
    url = Url.objects.all()
    return render(request, 'urlshortener/index.html')


def saveurl(request):
    return render(request, 'urlshortener/index.html')


