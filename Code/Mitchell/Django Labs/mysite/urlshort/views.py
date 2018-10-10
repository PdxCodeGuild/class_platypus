from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Url
import random, string

def index(request):
    urls = Url.objects.all()
    return render(request, 'urlshort/index.html', {'urls': urls})

def saveUrl(request):
    url_input = request.POST['url_input']
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    url = Url(long_url=url_input, short_url=code)
    url.save()
    return HttpResponseRedirect(reverse('urlshort:index'))

def redirect(request):
    return HttpResponseRedirect(reverse('render/url:long_url/'))

def clearUrls(request):
    urls = Url.objects.all()
    for url in urls:
        url.delete()
    return HttpResponseRedirect(reverse('urlshort:index'))