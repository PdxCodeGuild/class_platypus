from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from .models import Web_Url
import string

def index(request):
    return render(request, 'shorturl/index.html', {})


def add(request):
    user_url = request.POST['Web_Url']
    # generate the short code, save it with the model
    if request.method == 'POST':
        for i in range(5):
            code = random.choice(string.ascii_letters + string.digits)
            i += 1
            print(code)
    code = Web_Url(original_url=user_url)
    code.save()
    return HttpResponseRedirect(reverse('shorturl:index'))



