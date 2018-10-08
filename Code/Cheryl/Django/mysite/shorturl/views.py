from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import Web_Url
import string


def index(request):
    urls = Web_Url.objects.order_by('-id')
    return render(request, 'shorturl/index.html', {'urls': urls})


def add(request):
    user_url = request.POST['Web_Url']
    random_chars = ''
    for i in range(4):
        random_chars += random.choice(string.ascii_letters + string.digits)
    print(random_chars)
    code = Web_Url(code=random_chars, original_url=user_url)
    code.save()
    return HttpResponseRedirect(reverse('shorturl:index'))


def redirect(request):
    original_url = Web_Url(original_url=user_url, code=code)
    original_url.save()
    return HttpResponseRedirect(reverse('shorturl:index'))
