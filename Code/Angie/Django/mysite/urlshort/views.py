from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import UrlShort
from django.utils.crypto import get_random_string

from django.shortcuts import redirect as redirect_django




def index(request):
    longUrl = UrlShort.objects.all()
    return render(request, 'urlshort/index.html', {'longUrl': longUrl})

# save URL and create a code
def saveUrl(request):
    text = request.POST['text']
    text = text.lstrip('http://').lstrip('www.')
    print(text)
    short_url = UrlShort(long_url=text, code=get_random_string(6))
    short_url.save()
    return HttpResponseRedirect(reverse('urlshort:index'))

# find URL from code then redirect to the longURL
def redirect(request, code):
    if UrlShort.objects.filter(code=code).exists():
        record = UrlShort.objects.get(code=code)
        return redirect_django('http://www.' + record.long_url)
    return redirect_django('http://www.google.com/')




