from django.urls import path

from . import views


app_name = 'urlshortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('change/<short>', views.change, name='change'),
    path('clear_list/', views.clear_list, name='clear_list')
    ]
