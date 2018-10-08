from django.contrib import admin

from .models import Todolist, TodoListItem


admin.site.register(Todolist)
admin.site.register(TodoListItem)