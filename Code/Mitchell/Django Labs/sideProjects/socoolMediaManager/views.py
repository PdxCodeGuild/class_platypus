from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Platform, PlatformType
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'socoolMediaManager/index.html', {})

@login_required
def profile(request):
    platforms = request.user.platform_set.all()
    platform_types = PlatformType.objects.all()
    return render(request, 'socoolMediaManager/profile.html', {'platforms': platforms, 'platform_types': platform_types})

@login_required
def edit(request):
    platforms = request.user.platform_set.all()
    platform_types = PlatformType.objects.all()
    return render(request, 'socoolMediaManager/edit.html', {'platforms': platforms, 'platform_types': platform_types})

def addPlatform(request):
    link_input = request.POST['link_input']
    platform_type_id = request.POST['platform_type_id']
    platform = Platform(user=request.user, link=link_input, platform_type_id=platform_type_id)
    platform.save()
    return HttpResponseRedirect(reverse('socoolMediaManager:edit'))

def deletePlatform(request):
    id = request.POST['id']
    platform = Platform.objects.get(pk=id)
    platform.delete()
    return HttpResponseRedirect(reverse('socoolMediaManager:edit'))

def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, password)
    login(request, user)
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('socoolMediaManager:index'))
    return HttpResponseRedirect(reverse('socoolMediaManger:register'))

def register(request):
    return render(request, 'socoolMediaManager/register.html', {})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('socoolMediaManager:index'))
