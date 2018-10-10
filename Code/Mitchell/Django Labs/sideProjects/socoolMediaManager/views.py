from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Platform

def index(request):
    platforms = Platform.objects.all()
    return render(request, 'socoolMediaManager/index.html', {'platforms': platforms})

def edit(request):
    platforms = Platform.objects.all()
    return render(request, 'socoolMediaManager/edit.html', {'platforms': platforms})

def addPlatform(request):
    username_input = request.POST['username_input']
    link_input = request.POST['link_input']
    platform = Platform(username=username_input, link=link_input)
    platform.save()
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))

def deletePlatform(request):
    id = request.POST['id']
    platform = Platform.objects.get(pk=id)
    platform.delete()
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))