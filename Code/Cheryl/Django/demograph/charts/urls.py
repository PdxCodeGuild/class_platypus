from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'charts'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.get_data, name='get_data')

]