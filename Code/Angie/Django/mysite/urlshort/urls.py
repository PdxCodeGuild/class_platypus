from django.urls import path

from . import views

app_name = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
    # path('saveUrl/', views.saveUrl, name='saveUrl'),
    # path('redirect/', views.redirect, name='redirect')


]
