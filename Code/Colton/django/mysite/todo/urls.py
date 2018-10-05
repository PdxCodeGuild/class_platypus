
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.addtodo, name='addtodo'),
    path('deletetodo/', views.deletetodo, name='deletetodo'),
    path('clear_todo_list/', views.clear_todo_list, name='clear_todo_list')
    ]
