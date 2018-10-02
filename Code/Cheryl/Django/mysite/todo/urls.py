from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    # path('<int:TodoItem_id>/', views.index, name='index')

]