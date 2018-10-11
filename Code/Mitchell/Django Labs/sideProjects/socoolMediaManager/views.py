from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Platform, PlatformType

def index(request):
    platforms = Platform.objects.all()
    platform_types = PlatformType.objects.all()
    return render(request, 'socoolMediaManager/index.html', {'platforms': platforms, 'platform_types': platform_types})

def edit(request):
    platforms = Platform.objects.all()
    platform_types = PlatformType.objects.all()
    return render(request, 'socoolMediaManager/edit.html', {'platforms': platforms, 'platform_types': platform_types})

def addPlatform(request):
    username_input = request.POST['username_input']
    link_input = request.POST['link_input']
    platform_type_id = request.POST['platform_type_id']
    platform = Platform(username=username_input, link=link_input, platform_type_id=platform_type_id)
    platform.save()
    return HttpResponseRedirect(reverse('socoolMediaManager:edit'))

def deletePlatform(request):
    id = request.POST['id']
    platform = Platform.objects.get(pk=id)
    platform.delete()
    return HttpResponseRedirect(reverse('socoolMediaManager:edit'))