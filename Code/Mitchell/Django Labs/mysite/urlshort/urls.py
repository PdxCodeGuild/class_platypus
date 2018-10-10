from django.urls import path
from . import views

app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveUrl/', views.saveUrl, name='saveUrl'),
    path('clearUrls/', views.clearUrls, name='clearUrls'),
    path('redirect/<str:code>/', views.redirect, name='redirect'),
]