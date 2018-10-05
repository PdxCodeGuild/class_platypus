from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Platform

def index(request):
    #return HttpResponse("Hello, world. You're at the Socool Media Manager's index.")
    platforms = Platform.objects.all()
    return render(request, 'socoolMediaManager/index.html', {'platforms': platforms})

def addPlatform(request):
    username_input = request.POST['username_input']
    link_input = request.POST['link_input']
    platform = Platform(username=username_input, link=link_input)
    platform.save()
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))

def clearPlatforms(request):
    platforms = Platform.objects.all()
    for platform in platforms:
        platform.delete()
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))
