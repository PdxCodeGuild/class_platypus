
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.addtodo, name='addtodo'),
    ]
