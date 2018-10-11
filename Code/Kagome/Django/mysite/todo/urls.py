from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'todo'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('add/', views.add_todo, name='addtodo'),
    path('all/', views.all, name='all'),
    path('deletetodo/', views.deletetodo, name='deletetodo'),
    path('completetodo/', views.completetodo, name='completetodo'),
]
