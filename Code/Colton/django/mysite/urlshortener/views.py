from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
import random
import string

def index(request):
    urls = Url.objects.all()
    return render(request, 'urlshortener/index.html', {'urls': urls})


def saveurl(request):
    link = request.POST['link']
    short = ''
    for x in range(6):
        short += random.choice(string.ascii_letters)
    link = Url(link=link, short=short)
    link.save()
    return HttpResponseRedirect(reverse('urlshortener:index'))


