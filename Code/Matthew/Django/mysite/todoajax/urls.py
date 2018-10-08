
from django.urls import path

from . import views

app_name = 'todoajax'
urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('additem/', views.additem, name='additem'),
    path('getitems/', views.getitems, name='getitems')
]

