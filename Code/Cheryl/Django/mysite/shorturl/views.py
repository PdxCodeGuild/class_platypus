from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    return render(request, 'shorturl/index.html', {})


def add(request):
    user_url = request.POST['UserUrl']
    user_item = UserUrl(name=user_url)
    user_item.save()
    return HttpResponseRedirect(reverse('shorturl:index'))

