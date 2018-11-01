from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'charts'
urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.getdata, name='getdata'),

]