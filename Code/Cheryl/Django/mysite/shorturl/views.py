from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect


from .models import Web_Url

def index(request):
    return render(request, 'shorturl/index.html', {})


def add(request):
    user_url = request.POST['Web_Url']
    # generate the short code, save it with the model
    user_item = Web_Url(original_url=user_url)
    user_item.save()
    return HttpResponseRedirect(reverse('shorturl:index'))

